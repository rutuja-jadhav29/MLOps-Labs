from sklearn.tree import DecisionTreeClassifier
import joblib
from data import load_data, split_data

MODEL_PATH = "../model/bc_model.pkl"

def fit_model(X_train, y_train):
    """
    Train a Decision Tree Classifier and save the model to a file.
    """
    dt_classifier = DecisionTreeClassifier(max_depth=5, random_state=12)
    dt_classifier.fit(X_train, y_train)
    joblib.dump(dt_classifier, MODEL_PATH)

if __name__ == "__main__":
    X, y = load_data()
    X_train, X_test, y_train, y_test = split_data(X, y)
    fit_model(X_train, y_train)

