import logging


logger = logging.getLogger(__name__)
logger.addHandler(logging.FileHandler("package.log", "a"))
logger.setLevel(logging.INFO)
