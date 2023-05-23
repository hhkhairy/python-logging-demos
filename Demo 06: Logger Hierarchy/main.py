import logging

parent_logger = logging.getLogger("parent")
parent_logger.setLevel(logging.DEBUG)
parent_logger.addHandler(logging.StreamHandler())

child_logger = logging.getLogger("parent.child")
#child_logger.addHandler(logging.StreamHandler())
child_logger.debug("This is a debug message")
