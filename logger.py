from datetime import datetime
import logging
import sys

logging.SUCCESS = 25  # between WARNING and INFO
logging.addLevelName(logging.SUCCESS, 'SUCCESS')
logger = logging.getLogger(
    __name__
)

file_handler = logging.FileHandler(
    datetime.now().strftime("LOG(%m:%d:%Y)")
)
file_handler.setFormatter(
    logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s')
)
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setFormatter(
    logging.Formatter("%(levelname)s~$ %(message)s")
)
logger.setLevel(
    logging.DEBUG
)
logger.addHandler(
    stdout_handler
)
logger.addHandler(
    file_handler
)
setattr(
    logger,
    'success',
    lambda message, *args: logger._log(
        logging.SUCCESS,
        message,
        args
    )
)
