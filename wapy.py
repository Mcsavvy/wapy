from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Expect
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException
)
from time import sleep
import re
import sys
import os
from typing import Iterable
from logger import logger
from selenium.webdriver.chrome.options import Options
from waiting import wait, TimeoutExpired


class Wapy:
    processed = "processed.txt"
    success = "success.txt"

    def __init__(self, text=None):
        self.text = text
        self.session_started = False

    class Selectors:
        text_input = (
            "#main > footer > div.vR1LG._3wXwX.copyable-area > "
            "div._2A8P4 > div"
        )
        invalid_number = (
            "//*[contains(text(), "
            "'Phone number shared via url is invalid.')]"
        )

    def get_url(self, url):
        try:
            self.driver.execute_script(
                "window.onbeforeunload = function(){}"
            )
        except Exception:
            pass

        self.driver.get(url)

    def send_dm(self, text: str):
        text_input = self.driver.find_element_by_css_selector(
            self.Selectors.text_input
        )
        try:
            text_input.click()
            sleep(1)
        except Exception:
            pass

        def set_mock():
            self.driver.execute_script(
                "mock = document.getSelection({0})".format(
                    self.Selectors.text_input
                )

            )

        def get_mock():
            return self.driver.execute_script(
                "return mock.anchorNode.textContent"
            )

        set_mock()
        while get_mock() != text:
            text_input.send_keys(text)
        while get_mock() == text:
            text_input.send_keys(Keys.ENTER)

    def get_numbers(self, o):
        def _from_text(blob: str, this):
            pattern = re.compile(r"\+\d{1,3}\s?\d{10}")
            _ = [number.strip() for number in pattern.findall(blob)]
            # Removing Any Duplicates
            this.numbers = list(set(_))

        def _from_iter(iterable, this):
            this.numbers = list(set(iterable))

        def _from_file(path, this):
            with open(path) as f:
                blob = f.read()
            _from_text(blob, this)

        if isinstance(o, str):
            if os.path.isfile(o):
                return _from_file(o, self)
            return _from_text(o, self)
        elif isinstance(o, Iterable):
            return _from_iter(o, self)
        logger.error("Can't get numbers from %s", o)
        sys.exit()

    def create_link(self, phone_number: str):
        return (
            'https://web.whatsapp.com/send?phone={0}'.format(
                phone_number.strip('+')
            )
        )

    @staticmethod
    def on(event, handler, timeout, fail=None):
        try:
            wait(event, timeout_seconds=timeout)
            if callable(handler):
                return handler()
            return handler
        except TimeoutExpired:
            if callable(fail):
                return fail()
            return fail

    def destroy_link(self, link: str):
        index = link.find('=')
        number = link[index + 1:]
        return f'+{number}'

    def test_number(self, number):
        logger.info("Testing %s against whatsapp", number)
        target = self.create_link(number)
        self.get_url(target)
        while True:
            try:
                self.driver.find_element_by_css_selector(
                    self.Selectors.text_input
                )
                logger.info("Trigger Spotted")
                valid = True
                break
            except NoSuchElementException:
                pass

            try:
                self.driver.find_element_by_xpath(
                    self.Selectors.invalid_number
                )
                logger.info("Trigger Spotted")
                valid = False
                break
            except NoSuchElementException:
                pass
        if valid:
            logger.success("%s is valid", number)
            if self.text:
                self.send_dm(self.text)
            with open(self.success, "a+") as s:
                s.write(f"{number}\n")
        else:
            logger.error("%s is invalid", number)
        with open(self.processed, 'a+') as p:
            p.write(f"{number}\n")

    def end_session(self):
        logger.info("Session Stopped.")
        self.driver.quit()

    def start_session(self):
        if self.session_started:
            return
        logger.info("Session Started.")
        options = Options()
        # options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
        self.get_url("https://web.whatsapp.com")
        self.driver.get(
            "https://web.whatsapp.com"
        )
        try:
            Wait(self.driver, 10).until(
                Expect.presence_of_element_located(
                    (By.CSS_SELECTOR, "div.landing-main ._3jid7")
                )
            )
        except TimeoutException:
            self.end_session()
            return False
        self.driver.find_element_by_class_name(
            "landing-main"
        )
        sleep(5)
        logger.info("Scan QR Code.")
        logger.warning("Would Timeout In 20 seconds.")

        def redirected_to_dashboard():
            try:
                self.driver.find_element_by_class_name(
                    "landing-main"
                )
                return False
            except NoSuchElementException:
                return True

        # def refresh_qr():
        #     def qr():
        #         return self.driver.find_element_by_css_selector(
        #             "div.landing-main ._3jid7"
        #         )

        #     qr_data_ref = ""

        #     def set_qr():
        #         nonlocal qr_data_ref
        #         qr_data_ref = qr().get_attribute("data-ref")

        #     set_qr()

        #     def qr_changed():
        #         if qr().get_attribute(
        #             "data-ref"
        #         ) != qr_data_ref:
        #             return True
        #         return False
        #     self.on(
        #         qr_changed,
        #         set_qr,
        #         20
        #     )

        try:
            wait(
                redirected_to_dashboard,
                timeout_seconds=30,
                waiting_for="redirection to dashboard"
            )
            self.session_started = True
            return True
        except TimeoutExpired:
            logger.error("QR-Code timed-out.")
            self.end_session()
            return False

    def __call__(self, count=0, relaunch=True):
        if not getattr(self, 'numbers', None):
            logger.error("Numbers Have Not Been Added")
            sys.exit()
        if not self.start_session():
            sys.exit()
        if os.path.isfile(self.processed) and relaunch:
            logger.info(
                "Relaunch was set to True. "
                "Would relaunch if previous record is found."
            )
            with open(self.processed) as p:
                pread = p.read()
            if pread:
                numbers = []
                logger.info("Previous record discovered. Relaunching..")
                pattern = re.compile(r"\+\d{1,3}\s?\d{10}")
                _ = [number.strip() for number in pattern.findall(pread)]
                processed = list(set(_))
                for num in self.numbers:
                    if num not in processed:
                        numbers.append(num)
        numbers = list(set(locals().get("numbers", self.numbers)))
        logger.info("WA starting...")
        for number in numbers[count:]:
            self.test_number(number)
        logger.info("WA terminating...")
        self.end_session()
