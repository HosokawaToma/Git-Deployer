import logging
import os
import sys


class ApplicationLog:
    def __init__(self, log_file_path: str):
        self.log_file_path: str = log_file_path
        self.load()

    def load(self) -> None:
        if self.log_file_path is None:
            raise ValueError("Log file path is required")
        if not os.path.exists(self.log_file_path):
            os.makedirs(os.path.dirname(self.log_file_path), exist_ok=True)
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.log_file_path),
                logging.StreamHandler(sys.stdout)
            ]
        )

    def info(self, message: str) -> None:
        logging.info(message)

    def error(self, message: str) -> None:
        logging.error(message)

    def warning(self, message: str) -> None:
        logging.warning(message)

    def debug(self, message: str) -> None:
        logging.debug(message)
