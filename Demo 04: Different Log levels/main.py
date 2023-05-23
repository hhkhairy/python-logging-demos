import logging

#logging.basicConfig()
logger_debug = logging.getLogger("some logger")
logger_debug.setLevel(logging.DEBUG)
logger_debug.addHandler(logging.StreamHandler())

logger_info = logging.getLogger("another logger")
logger_info.setLevel(logging.INFO)
logger_info.addHandler(logging.StreamHandler())

logger_debug.debug("This is a debug message")
logger_info.debug("This is a debug message. It won't be printed.")