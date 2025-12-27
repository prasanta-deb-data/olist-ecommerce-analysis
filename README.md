

# Olist E-commerce Orders & Payment Analysis

## 📌 Project Overview
This project analyzes customer order and payment behavior for **Olist**, a Brazilian e-commerce marketplace.  
The primary focus is to understand **payment patterns**, especially **credit card usage**, and identify **monthly revenue trends** to support business and risk-related decisions.

The solution is built as a **modular, production-style Python pipeline** with configuration management and logging.

---

## 🎯 Business Objectives
- Combine multiple transactional datasets into a single analytical dataset  
- Perform light but meaningful data cleaning and transformation  
- Analyze payment value distribution across different payment methods  
- Evaluate whether credit card payments result in higher transaction values  
- Identify monthly and seasonal trends in total payment value  
- Deliver reusable outputs suitable for reporting and dashboards  

---

## 📂 Dataset Description
The analysis is based on three datasets provided by Olist:

| File Name | Description |
|---------|------------|
| `orders.xlsx` | Order-level information including purchase timestamps |
| `order_payment.xlsx` | Payment details such as payment type and value |
| `customers.xlsx` | Customer-level information |

All raw datasets are kept unchanged and stored separately from processed data.

---

## 🧱 Project Structure
olist-ecommerce-analysis/
│
├── config/
│ └── config.yaml # Centralized configuration
│
├── data/
│ ├── raw/ # Original source data
│ │ ├── orders.xlsx
│ │ ├── order_payment.xlsx
│ │ └── customers.xlsx
│ └── processed/ # Cleaned & merged dataset
│
├── scripts/
│ ├── init.py
│ ├── logger.py # Centralized logging
│ ├── config_loader.py # YAML config loader
│ ├── load_data.py
│ ├── clean_merge.py
│ ├── payment_analysis.py
│ ├── monthly_analysis.py
│ └── main.py # Pipeline orchestrator
│
├── outputs/
│ ├── tables/ # Final analytical tables
│ └── charts/ # Visualizations
│
├── logs/
│ └── pipeline.log # Execution logs
│
├── requirements.txt
├── .gitignore
└── README.md

yaml
Copy code

---

## 🔄 Data Pipeline Workflow
1. **Data Ingestion**
   - Load raw Excel datasets using pandas
   - Paths managed via `config.yaml`

2. **Data Integration & Cleaning**
   - Join orders, payments, and customers datasets
   - Convert timestamps and derive month-level features
   - Remove invalid or incomplete payment records

3. **Analytical Processing**
   - Payment value range by payment type
   - Credit card vs non-credit card behavior analysis
   - Monthly payment trends by payment type
   - Total monthly payment value analysis

4. **Output Generation**
   - CSV summary tables
   - PNG charts for reporting and dashboards
   - Detailed execution logs

---

## 📊 Key Insights
- Credit card payments have **higher average and maximum transaction values**
- Credit cards contribute the **largest share of monthly revenue**
- Clear **seasonality patterns** are observed in total payment value
- Payment method analysis highlights potential **credit exposure risks**

---

## 🛠️ Tech Stack
- **Language:** Python  
- **Libraries:** pandas, matplotlib, seaborn, PyYAML  
- **Data Format:** Excel, CSV  
- **Version Control:** Git & GitHub  

---

## ▶️ How to Run the Project
From the project root directory:

```bash
pip install -r requirements.txt
python scripts/main.py

After execution, results will be available in:

data/processed/

outputs/tables/

outputs/charts/

logs/pipeline.log

----

🚀 Future Enhancements
SQL-based transformation layer (PostgreSQL)

Power BI dashboard for business users

Automated scheduling using Airflow

Data validation using Pandera or Great Expectations

👤 Author
Prasanta Kumar Deb
Data Analyst | Python | SQL | Power BI
