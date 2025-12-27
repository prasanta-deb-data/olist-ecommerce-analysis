import pandas as pd
from pathlib import Path
from logger import get_logger
from config_loader import load_config

logger = get_logger(__name__)
config = load_config()

BASE_DIR = Path(__file__).resolve().parent.parent

def load_data():
    logger.info("Loading raw datasets")

    orders = pd.read_excel(
        BASE_DIR / config["paths"]["raw_data"]["orders"]
    )
    payments = pd.read_excel(
        BASE_DIR / config["paths"]["raw_data"]["payments"]
    )
    customers = pd.read_excel(
        BASE_DIR / config["paths"]["raw_data"]["customers"]
    )

    logger.info("Raw datasets loaded successfully")
    return orders, payments, customers
