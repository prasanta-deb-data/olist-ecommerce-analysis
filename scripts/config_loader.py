import yaml
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "config/config.yaml"

def load_config():
    with open(CONFIG_PATH, "r") as file:
        config = yaml.safe_load(file)
    return config
