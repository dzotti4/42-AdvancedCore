import pandas as pd


def load(path: str):
    """Load a CSV file and return it as a panda DataFrame."""
    try:
        dataset = pd.read_csv(path)
        print(f"Loading dataset of dimensions {dataset.shape}")
        return dataset
    except Exception:
        return None
