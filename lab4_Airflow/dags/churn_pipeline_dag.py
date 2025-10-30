from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os

# -----------------------------
# Step 1 — Load & Save Data
# -----------------------------
def load_data():
    url = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"
    df = pd.read_csv(url)
    os.makedirs("/opt/airflow/working_data", exist_ok=True)
    df.to_csv("/opt/airflow/working_data/churn_raw.csv", index=False)
    print(f"✅ Data downloaded — {df.shape[0]} rows, {df.shape[1]} cols")

# -----------------------------
# Step 2 — Preprocess Data
# -----------------------------
def preprocess_data():
    df = pd.read_csv("/opt/airflow/working_data/churn_raw.csv")

    # Drop customerID column
    df.drop("customerID", axis=1, inplace=True)

    # Convert TotalCharges to numeric
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df.fillna(df["TotalCharges"].median(), inplace=True)

    # Encode categorical variables
    for col in df.select_dtypes(include=["object"]).columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])

    df.to_csv("/opt/airflow/working_data/churn_processed.csv", index=False)
    print(f"✅ Data preprocessed — saved to churn_processed.csv")

# -----------------------------
# Step 3 — Train Model
# -----------------------------
def train_model():
    df = pd.read_csv("/opt/airflow/working_data/churn_processed.csv")
    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    model = RandomForestClassifier(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)

    os.makedirs("/opt/airflow/working_data/model", exist_ok=True)
    with open("/opt/airflow/working_data/model/churn_model.pkl", "wb") as f:
        pickle.dump(model, f)

    print("✅ Model trained and saved as churn_model.pkl")

# -----------------------------
# Step 4 — Evaluate Model
# -----------------------------
def evaluate_model():
    df = pd.read_csv("/opt/airflow/working_data/churn_processed.csv")
    X = df.drop("Churn", axis=1)
    y = df["Churn"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    with open("/opt/airflow/working_data/model/churn_model.pkl", "rb") as f:
        model = pickle.load(f)

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    report = classification_report(y_test, preds)

    print(f"✅ Model Accuracy: {acc:.3f}")
    print("📊 Classification Report:\n", report)

# -----------------------------
# DAG Definition
# -----------------------------
default_args = {
    'owner': 'rutuja',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

with DAG(
    dag_id='customer_churn_ml_pipeline',
    default_args=default_args,
    description='End-to-end ML pipeline for churn prediction',
    schedule_interval=None,  # Run manually
    start_date=datetime(2025, 10, 26),
    catchup=False,
    tags=['ml', 'churn', 'demo'],
) as dag:

    task_load = PythonOperator(
        task_id='load_data',
        python_callable=load_data,
    )

    task_prep = PythonOperator(
        task_id='preprocess_data',
        python_callable=preprocess_data,
    )

    task_train = PythonOperator(
        task_id='train_model',
        python_callable=train_model,
    )

    task_eval = PythonOperator(
        task_id='evaluate_model',
        python_callable=evaluate_model,
    )

    # DAG dependencies
    task_load >> task_prep >> task_train >> task_eval
