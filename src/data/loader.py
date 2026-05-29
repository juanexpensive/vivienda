import pandas as pd
from pathlib import Path

data_path = Path("data") / "housing_sample.csv"

def load_housing_data() -> pd.DataFrame:
    housing_data = pd.read_csv(data_path)
    return housing_data

