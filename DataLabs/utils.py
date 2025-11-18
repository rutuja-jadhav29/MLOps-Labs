"""
Utility functions for Snorkel IMDB Sentiment Lab
------------------------------------------------
Contains helpers for:
- Text cleaning
- Dataset loading and concatenation
- Basic EDA (label plot)
"""

import re
import os
import glob
import pandas as pd
import matplotlib.pyplot as plt


# ----------------------------------------------------
# TEXT CLEANING
# ----------------------------------------------------
def clean_text(s: str) -> str:
    """Basic text cleaner: lowercase + remove symbols + normalize spaces."""
    s = s.lower()
    s = re.sub(r"[^a-z0-9\s?!\-]", " ", s)   # keep letters, numbers, ? ! -
    s = re.sub(r"\s+", " ", s).strip()
    return s


# ----------------------------------------------------
# DATA LOADER
# ----------------------------------------------------
def load_datasets(path: str) -> pd.DataFrame:
    """
    Loads ALL .csv files from a folder and returns a combined dataframe.
    Expected columns: 'text', 'label'
    Adds 'text_clean' column for modeling.
    """
    files = sorted(glob.glob(os.path.join(path, "*.csv")))
    if not files:
        raise FileNotFoundError(f"No CSV files found in folder: {path}")

    frames = [pd.read_csv(f) for f in files]
    df = pd.concat(frames, ignore_index=True)

    # Validate columns
    if "text" not in df.columns:
        raise ValueError("Dataset missing 'text' column")
    if "label" not in df.columns:
        raise ValueError("Dataset missing 'label' column")

    # Clean text
    df["text_clean"] = df["text"].astype(str).map(clean_text)

    return df


# ----------------------------------------------------
# SIMPLE VISUALIZATION
# ----------------------------------------------------
def plot_label_counts(df, col="label"):
    """Plot bar chart of label distribution."""
    ax = df[col].value_counts().sort_index().plot(kind="bar")
    ax.set_xlabel(col)
    ax.set_ylabel("Count")
    ax.set_title("Label Distribution")
    plt.tight_layout()
    return ax
