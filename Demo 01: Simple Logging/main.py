import logging


logger = logging.getLogger("some logger")
logger.addHandler(logging.StreamHandler())

logger.error("This is an error message")