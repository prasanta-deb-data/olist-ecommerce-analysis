import matplotlib.pyplot as plt
from pathlib import Path
from logger import get_logger
from config_loader import load_config

logger = get_logger(__name__)
config = load_config()

BASE_DIR = Path(__file__).resolve().parent.parent

def monthly_analysis(df):
    logger.info("Starting monthly analysis")

    try:
        figsize = (
            config["plots"]["figsize"]["width"],
            config["plots"]["figsize"]["height"]
        )

        # ---- Monthly payment by type ----
        monthly_payment_type = df.groupby(
            ["order_month", "payment_type"]
        )["payment_value"].sum().reset_index()

        monthly_payment_type.to_csv(
            BASE_DIR / config["paths"]["outputs"]["tables"] / "monthly_payment_type.csv",
            index=False
        )

        pivot_df = monthly_payment_type.pivot(
            index="order_month",
            columns="payment_type",
            values="payment_value"
        )

        plt.figure(figsize=figsize)
        pivot_df.plot()
        plt.title("Monthly Payment Value by Payment Type")
        plt.tight_layout()

        plt.savefig(
            BASE_DIR / config["paths"]["outputs"]["charts"] / "monthly_payment_by_type.png"
        )
        plt.close()

        logger.info("Monthly payment by type chart saved")

        # ---- Monthly total payment ----
        monthly_total = df.groupby("order_month")["payment_value"].sum()

        monthly_total.to_csv(
            BASE_DIR / config["paths"]["outputs"]["tables"] / "monthly_total_payment.csv"
        )

        plt.figure(figsize=figsize)
        monthly_total.plot()
        plt.title("Total Payment Value by Month")
        plt.tight_layout()

        plt.savefig(
            BASE_DIR / config["paths"]["outputs"]["charts"] / "monthly_total_payment.png"
        )
        plt.close()

        logger.info("Monthly total payment chart saved")

    except Exception:
        logger.error("Error in monthly analysis", exc_info=True)
        raise
