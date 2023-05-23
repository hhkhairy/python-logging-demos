import logging

root_logger = logging.getLogger("")
root_logger.error("An error message")


logging.basicConfig()
root_logger.error("An error message")
# Sets a fomatter for the root logger
# Sets a StreamHandler for the root logger, with the aforementioned formatter
# ... unless the logger has a handler already