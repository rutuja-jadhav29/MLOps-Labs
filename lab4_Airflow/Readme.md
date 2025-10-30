## **Project Overview**

This project demonstrates an end-to-end Machine Learning workflow orchestrated with Apache Airflow.
The pipeline automates the process of loading, preprocessing, training, and evaluating a customer churn prediction model — a critical business problem for telecom and subscription-based companies.

## Project Structure
```bash
lab4_Airflow/
│
├── dags/
│   └── churn_pipeline_dag.py         # Airflow DAG defining the ML pipeline
│
├── working_data/
│   ├── churn_raw.csv                 # Raw dataset before preprocessing
│   └── churn_processed.csv           # Cleaned dataset used for training
│
├── docker-compose.yaml               # Airflow environment setup using Docker
├── .gitignore                        # Git ignore file
└── Readme.md                         # Project documentation
```
## Pipeline Overview

**DAG Name:** customer_churn_ml_pipeline 

This DAG contains four main tasks:
| Task Name         | Description                                                                |
| ----------------- | -------------------------------------------------------------------------- |
| `load_data`       | Loads raw churn dataset into the pipeline                                  |
| `preprocess_data` | Cleans and transforms raw data for modeling                                |
| `train_model`     | Trains a machine learning model (e.g., Logistic Regression / RandomForest) |
| `evaluate_model`  | Evaluates the model and logs accuracy, precision, recall, and F1-score     |

Model Accuracy: 0.786

Macro F1-Score: 0.70
(Logged in Airflow task logs)


## Key Features

- Modular Airflow DAG: Each step of the ML pipeline is orchestrated as a separate Airflow task.

- Reproducible Workflow: Uses Docker Compose to spin up Airflow containers.

- Automated Logging: Model evaluation metrics (accuracy, precision, recall, F1) are logged for each run.

- Dataset Versioning: Intermediate files (churn_raw.csv, churn_processed.csv) stored for reproducibility.

- Scalable Design: Can easily extend to add hyperparameter tuning, model registry, or cloud storage.

## How to Run

1. Clone the Repository

```bash
git clone <repo_url>
cd lab4_Airflow
```
2. Start Airflow with Docker
   
```bash
docker-compose up -d
```
Airflow Web UI will be available at:
http://localhost:8080

3. Access Airflow Dashboard

Username: airflow

Password: airflow

4. Trigger the DAG

Turn on the DAG: customer_churn_ml_pipeline

Click Trigger DAG

Monitor task progress via Graph View or Logs

<img width="1232" height="335" alt="Screenshot 2025-10-26 at 11 06 43 AM" src="https://github.com/user-attachments/assets/1f7f6f29-7484-4490-9eec-b3776ae92537" />

<img width="1236" height="563" alt="Screenshot 2025-10-26 at 11 07 09 AM" src="https://github.com/user-attachments/assets/5ef6e099-057d-4c67-b60a-6a629e239d3c" />

<img width="1044" height="236" alt="Screenshot 2025-10-26 at 11 07 36 AM" src="https://github.com/user-attachments/assets/5633905d-86ac-42ad-b418-a3d00e573fe7" />

## Technologies Used

Apache Airflow (workflow orchestration)

Python (data preprocessing, model training)

scikit-learn (ML model)

Docker & Docker Compose (containerization)

Pandas / NumPy (data wrangling)


