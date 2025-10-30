import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

def load_data():
    """
    Load the Breast Cancer dataset and return the features and target values.
    Returns:
        X (numpy.ndarray): Feature matrix.
        y (numpy.ndarray): Target labels (0 = malignant, 1 = benign).
    """
    bc = load_breast_cancer()
    X = bc.data
    y = bc.target
    return X, y

def split_data(X, y):
    """
    Split the data into training and testing sets.
    """
    return train_test_split(X, y, test_size=0.3, random_state=12)
