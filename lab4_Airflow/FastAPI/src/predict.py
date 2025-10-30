import joblib

MODEL_PATH = "../model/bc_model.pkl"

def predict_data(X):
    """
    Predict malignant (0) or benign (1) given input features.
    Args:
        X (numpy.ndarray): Input feature array.
    Returns:
        y_pred (numpy.ndarray): Predictions.
    """
    model = joblib.load(MODEL_PATH)
    return model.predict(X)

