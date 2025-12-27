from load_data import load_data
from clean_merge import clean_and_merge
from payment_analysis import payment_range_analysis
from monthly_analysis import monthly_analysis
from logger import get_logger

logger = get_logger(__name__)

def main():
    logger.info("Olist E-commerce Analysis Pipeline Started")

    try:
        orders, payments, customers = load_data()
        df = clean_and_merge(orders, payments, customers)
        payment_range_analysis(df)
        monthly_analysis(df)

        logger.info("Olist E-commerce Analysis Pipeline Completed Successfully")

    except Exception:
        logger.critical("Pipeline failed due to an error", exc_info=True)

if __name__ == "__main__":
    main()
