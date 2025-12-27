import logging
from pathlib import Path
from config_loader import load_config

config = load_config()

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_FILE = BASE_DIR / config["logging"]["file"]

LOG_FILE.parent.mkdir(exist_ok=True)

def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(config["logging"]["level"])

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        file_handler = logging.FileHandler(LOG_FILE)
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
