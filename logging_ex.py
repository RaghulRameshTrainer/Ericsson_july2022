import logging
'''
DEBUG       10
INFO        20
WARNING     30
ERROR       40
CRITICAL    50
'''
logging.basicConfig(filename='output.log',
                    level=logging.DEBUG,
                    format="%(levelname)s %(asctime)s - %(message)s")
logger=logging.getLogger()

logger.debug("simple debug message")
logger.info("just an info message")
logger.warning("warning message")
logger.error("issue an erorr message")
logger.critical("very critical message")