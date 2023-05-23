import logging
import my_module


logger = logging.getLogger("a dummy logger")
id1 = id(logger)
other_logger = my_module.get_logger()
id2 = id(other_logger)

print(id1 == id2)