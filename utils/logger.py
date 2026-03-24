import logging
import sys

def get_logger(name="api-tests"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(message)s"
    ))

    if not logger.handlers:
        logger.addHandler(handler)

    return logger