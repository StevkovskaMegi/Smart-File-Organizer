import logging
from datetime import datetime

class MoveLogger:
    def __init__(self, log_file='organizer.log'):
        self.logger = logging.getLogger("FileOrganizerLogger")
        self.logger.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(message)s')

        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)

        if not self.logger.handlers:
            self.logger.addHandler(file_handler)

    def log_move(self, source: str, destination: str):
        self.logger.info(f"Moved from: {source} → {destination}")
