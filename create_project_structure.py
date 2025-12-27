from pathlib import Path

# Base project directory
BASE_DIR = Path("C:/Portfolio/olist-ecommerce-analysis")

# Folder structure
folders = [
    BASE_DIR / "data/raw",
    BASE_DIR / "data/processed",
    BASE_DIR / "scripts",
    BASE_DIR / "outputs/tables",
    BASE_DIR / "outputs/charts",
    BASE_DIR / "notebooks"
]

# Files to create (including the 3 raw files)
files = {
    # RAW DATA FILE PLACEHOLDERS
    BASE_DIR / "data/raw/orders.xlsx": "",
    BASE_DIR / "data/raw/order_payment.xlsx": "",
    BASE_DIR / "data/raw/customers.xlsx": "",

    # PYTHON SCRIPTS
    BASE_DIR / "scripts/__init__.py": "",
    BASE_DIR / "scripts/load_data.py": "",
    BASE_DIR / "scripts/clean_merge.py": "",
    BASE_DIR / "scripts/payment_analysis.py": "",
    BASE_DIR / "scripts/monthly_analysis.py": "",
    BASE_DIR / "scripts/main.py": "",

    # PROJECT FILES
    BASE_DIR / "README.md": "# Olist E-commerce Orders Analysis\n",
    BASE_DIR / "requirements.txt": (
        "pandas\n"
        "matplotlib\n"
        "seaborn\n"
        "openpyxl\n"
    ),
    BASE_DIR / ".gitignore": (
        "__pycache__/\n"
        ".ipynb_checkpoints/\n"
        ".env\n"
    )
}

def create_structure():
    # Create folders
    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)

    # Create files
    for file_path, content in files.items():
        file_path.parent.mkdir(parents=True, exist_ok=True)
        if not file_path.exists():
            file_path.write_text(content)

    print("✅ Project structure created successfully!")
    print(f"📁 Location: {BASE_DIR}")
    print("📄 Raw files expected:")
    print("   - orders.xlsx")
    print("   - order_payment.xlsx")
    print("   - customers.xlsx")

if __name__ == "__main__":
    create_structure()
