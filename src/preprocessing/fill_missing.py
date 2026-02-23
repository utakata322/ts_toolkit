import pandas as pd


def fill_missing_data(data: pd.DataFrame) -> pd.DataFrame:
    data = data.fillna(data.mean())
    return data
