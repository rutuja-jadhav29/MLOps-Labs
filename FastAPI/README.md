**FastAPI Lab – Breast Cancer Prediction API**

***Overview***

In this lab, we learn how to expose **Machine Learning models as REST APIs** using **FastAPI** and **Uvicorn**.

- **FastAPI** → A modern, high-performance web framework for building APIs with **automatic data validation**, **type hints**, and **interactive documentation (Swagger UI)**.  
- **Uvicorn** → A lightning-fast ASGI (Asynchronous Server Gateway Interface) web server commonly used to serve FastAPI applications in production.


***Workflow***

1. Train a **classification model** (e.g., Logistic Regression or Random Forest) on the **Breast Cancer dataset** from `scikit-learn`.  
2. Save the trained model as a serialized `.pkl` file in the `model` directory.  
3. Serve the model as an API using **FastAPI + Uvicorn**.  
4. Expose endpoints for **real-time predictions** via `/predict`.  
5. Test API responses through **Swagger UI** or `curl`.


## 🧱 Project Structure
```bash
FastAPI/
├── assets/
│ ├── img1.png # (optional) Screenshot of running API
│ └── img2.png
│
├── model/
│ └── bc_model.pkl # Trained Breast Cancer model
│
├── src/
│ ├── init.py
│ ├── data.py # Data loading and preprocessing
│ ├── train.py # Model training and saving logic
│ ├── predict.py # Loads model and predicts from input JSON
│ ├── main.py # FastAPI application
│ 
│── requirements.txt # Dependencies
└── README.md # Main documentation file
```



---

## 🧰 Setting Up the Lab

### 1️⃣ Create and Activate Virtual Environment
```bash
python3 -m venv fastapi_env
source fastapi_env/bin/activate       # for macOS/Linux
fastapi_env\Scripts\activate          # for Windows

```

### 2️⃣ Install Dependencies
```bash
pip install -r src/requirements.txt

```

###  3️⃣ Train the Model
Run the training script to generate and save the model:

```bash
python src/train.py

```

### 4️⃣ Start the FastAPI Server

```bash
uvicorn src.main:app --reload

```


### 5️⃣ Test the API
Using Swagger UI

Go to http://127.0.0.1:8000/docs

You’ll see interactive endpoints:

GET / → Health check

POST /predict → Model prediction endpoint




### Understanding Each File

| File               | Description                               |
| ------------------ | ----------------------------------------- |
| `data.py`          | Loads and preprocesses the dataset        |
| `train.py`         | Trains ML model and saves it as `.pkl`    |
| `predict.py`       | Loads saved model and runs inference      |
| `main.py`          | Exposes FastAPI routes `/` and `/predict` |
| `bc_model.pkl`     | Serialized trained model                  |
| `requirements.txt` | List of dependencies                      |
| `assets/img1.png`  | Optional screenshots of UI/API            |




### Summary

This lab demonstrates how to deploy a machine learning model using FastAPI.
It covers:

Building a model from scratch

Serving it as a real-time API

Testing endpoints interactively

Building the foundation for MLOps automation.
