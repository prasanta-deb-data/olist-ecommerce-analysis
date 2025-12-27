import pandas as pd
from pathlib import Path
from logger import get_logger
from config_loader import load_config

logger = get_logger(__name__)
config = load_config()

BASE_DIR = Path(__file__).resolve().parent.parent

def clean_and_merge(orders, payments, customers):
    logger.info("Starting merge and cleaning process")

    df = orders.merge(payments, on="order_id", how="left")
    df = df.merge(customers, on="customer_id", how="left")

    df["order_purchase_timestamp"] = pd.to_datetime(
        df["order_purchase_timestamp"]
    )
    df["order_month"] = df["order_purchase_timestamp"].dt.to_period("M")

    df = df[df["payment_value"] > 0]
    df.dropna(subset=["payment_type"], inplace=True)

    output_path = BASE_DIR / config["paths"]["processed_data"]["merged"]
    df.to_csv(output_path, index=False)

    logger.info(f"Processed data saved at {output_path}")
    return df
