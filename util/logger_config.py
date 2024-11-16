## developed by sameera
import logging


def setup_logger():

    logger = logging.getLogger('QuoteLogger')
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)  # Set the log level

        # Console handler to output logs to the console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)

    return logger
