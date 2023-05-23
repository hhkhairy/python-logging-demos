import logging

logger = logging.getLogger("some logger")
logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
fomatter = logging.Formatter("Format 1: %(asctime)s - %(name)s - %(levelname)s - %(message)s")
stream_handler.setFormatter(fomatter)

stream_handler2 = logging.StreamHandler()
formatter2 = logging.Formatter("Format 2: %(asctime)s - %(name)s - %(levelname)s - %(message)s - %(filename)s - %(funcName)s - %(lineno)d")
stream_handler2.setFormatter(formatter2)

logger.addHandler(stream_handler)
logger.addHandler(stream_handler2)

logger.debug("This is a debug message")

