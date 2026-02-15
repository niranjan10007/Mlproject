from src.logger import logging
from src.exception import CustomException
import sys

if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.error("Exception occurred during testing", exc_info=True)
        raise CustomException(e, sys)
