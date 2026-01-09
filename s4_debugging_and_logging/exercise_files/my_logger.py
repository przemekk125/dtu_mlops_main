from loguru import logger
import sys

logger.remove()
logger.add("my_log.log", level="DEBUG", rotation="100 MB")

logger.debug("Used for debugging your code.")
logger.info("Informative messages from your code.")
logger.warning("Everything works but there is something to be aware of.")
logger.error("There's been a mistake with the process.")
logger.critical("There is something terribly wrong and process may terminate.")
