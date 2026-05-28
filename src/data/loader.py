import pandas as pd
from pathlib import Path


data_path = Path("data") / "housing_sample.csv"
def load_housing_data():
    read_data = pd.read_csv(data_path) 
    return read_data
