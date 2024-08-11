import logging
from config.settings import LOG_LEVEL

def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL)
    
    handler = logging.StreamHandler()
    handler.setLevel(LOG_LEVEL)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    return logger
