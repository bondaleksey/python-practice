import logging

logging.basicConfig(
    filename="log_filename.txt",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logging.debug("This is a log message.")
