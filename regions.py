import random
import json


class RandomPhoneNumbers:
    country_code = "+0"
    area_code = ['***']
    length = 10

    def get_iter(self, amount=1):
        for _ in range(amount):
            number = str(random.choice(self.area_code))
            empty_blocks = self.length - len(number)
            for _ in range(empty_blocks):
                number += str(random.randint(0, 9))
            number = self.country_code + number
            yield number

    def get_json(self, amount=1):
        numbers = list(self.get_iter(amount=amount))
        return json.dumps(numbers)

    def get_str(self, amount=1, sep=", "):
        numbers = list(self.get_iter(amount=amount))
        return sep.join(numbers)


class China(RandomPhoneNumbers):
    country_code = "+86"
    area_code = [10]


class USA(RandomPhoneNumbers):
    country_code = "+1"
    area_code = [951]


class Canada(USA):
    area_code = [613555]


class Newyork(USA):
    area_code = [718]


class Florida(USA):
    area_code = [813, 231]


class France(RandomPhoneNumbers):
    country_code = "+33"
    area_code = [93]


class Alabama(USA):
    area_code = [312]


class Arkansas(USA):
    area_code = [231]


class Georgia(USA):
    area_code = [678]


class UK(RandomPhoneNumbers):
    country_code = "+44"
    area_code = [71, 73, 74, 75, 76, 77, 78, 79]


class London(UK):
    area_code = [20]


class Australia(RandomPhoneNumbers):
    country_code = "+61"
    area_code = [61]


class Nigeria(RandomPhoneNumbers):
    country_code = "+234"
    area_code = [
        701, 7020, 7025, 7026, 7027,
        7028, 7029, 703, 704, 705, 706,
        707, 708, 709, 802, 803, 804, 805,
        806, 807, 808, 8099, 810, 811, 812,
        813, 814, 815, 816, 8179, 8189, 819,
        9099, 9089, 901, 902, 903, 904, 905,
        906, 907
    ]