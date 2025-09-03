from loguru import logger

logger.add("shipic.log", rotation="1 week", retention="4 weeks", compress=True, level="INFO")
