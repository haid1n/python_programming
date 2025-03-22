import logging

logging.basicConfig(filename="file_io/log_file.log", level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")

logging.info("Application started.")

logging.warning("Low disk space.")

logging.error("Error connecting to database.")

logging.critical("Application crashed.")

print("All logs have been written to log_file.log")

