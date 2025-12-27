import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from logger import get_logger
from config_loader import load_config

logger = get_logger(__name__)
config = load_config()

BASE_DIR = Path(__file__).resolve().parent.parent

def payment_range_analysis(df):
    logger.info("Starting payment range analysis")

    try:
        payment_range = df.groupby("payment_type")["payment_value"].agg(
            min_payment="min",
            max_payment="max",
            avg_payment="mean"
        ).reset_index()

        payment_range.to_csv(
            BASE_DIR / config["paths"]["outputs"]["tables"] / "payment_range_by_type.csv",
            index=False
        )

        logger.info("Payment range table saved")

        # ✅ FIGSIZE COMES FROM CONFIG HERE
        figsize = (
            config["plots"]["figsize"]["width"],
            config["plots"]["figsize"]["height"]
        )

        plt.figure(figsize=figsize)
        sns.boxplot(data=df, x="payment_type", y="payment_value")
        plt.xticks(rotation=45)
        plt.title("Payment Value Distribution by Payment Type")
        plt.tight_layout()

        plt.savefig(
            BASE_DIR / config["paths"]["outputs"]["charts"] / "payment_distribution.png"
        )
        plt.close()

        logger.info("Payment distribution chart saved")

    except Exception:
        logger.error("Error in payment analysis", exc_info=True)
        raise
