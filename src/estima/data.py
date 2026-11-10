from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT / "data" / "processed" / "tehran_houses_clean.csv"


def load_data() -> pd.DataFrame:
    """Load the cleaned Tehran housing dataset."""
    return pd.read_csv(DATA_PATH)


def split_data(
    df: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Split the dataset into training and testing sets."""

    X = df.drop(columns=["Price"])
    y = df["Price"]

    return train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )