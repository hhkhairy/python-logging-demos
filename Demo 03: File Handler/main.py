import logging
import sys

logger = logging.getLogger("some logger")
file_handler = logging.FileHandler("my_log.log", "w")
stream_handler = logging.StreamHandler(sys.stderr)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger.error("This is an error message 2")



'''
IF there's no handler, something like a stream handler will be used.
If there's a handler, other than the streaming one, the streaming one will not be used.
'''