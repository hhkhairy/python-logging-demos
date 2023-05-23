import logging
from package.module_1 import some_function

entry_logger = logging.getLogger("entry logger")
entry_logger.addHandler(logging.StreamHandler())
entry_logger.info("this message won't be printed")

module_logger = logging.getLogger("package.module_1")
print(module_logger.getEffectiveLevel())
print(entry_logger.getEffectiveLevel())

entry_logger.info("this message will not be printed")
some_function()


