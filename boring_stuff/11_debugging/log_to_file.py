import logging

logging.basicConfig(
    filename="log_prog_name.py",
    level=logging.INFO,
    format=" %(asctime)s - %(levelname)s - %(message)s",
)

logging.debug("Some debugging details #1.")
logging.info("The logging module is working #1.")
logging.warning("An error message is about to be logged #1.")
logging.error("An error has occurred #1.")
logging.critical("The program is unable to recover! #1")
logging.disable(logging.WARNING)
logging.debug("Some debugging details #2.")
logging.info("The logging module is working #2.")
logging.warning("An error message is about to be logged #2.")
logging.error("An error has occurred #2.")
logging.critical("The program is unable to recover! #2")
