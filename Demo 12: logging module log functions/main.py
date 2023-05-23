import logging


logging.error("An error message")

# The logging log functions call the root logger
# They also call the basicConfig() function if it hasn't been called yet
# That's why the log messages are formatted nicely, and they show the root logger as the one that logged them