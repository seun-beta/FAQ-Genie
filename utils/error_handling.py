from utils.logger import setup_logger

logger = setup_logger(__name__)

class CustomError(Exception):
    pass

def handle_error(e):
    logger.error(f"An error occurred: {str(e)}")
    raise CustomError(f"An unexpected error occurred: {str(e)}")
