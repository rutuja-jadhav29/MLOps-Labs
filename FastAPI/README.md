**FastAPI Lab – Breast Cancer Prediction API**

***Overview***

In this lab, we learn how to expose Machine Learning models as REST APIs using FastAPI and Uvicorn.

FastAPI → A modern, high-performance Python web framework for building APIs with automatic data validation and documentation.

Uvicorn → A lightning-fast ASGI (Asynchronous Server Gateway Interface) web server commonly used to serve FastAPI applications.

***Workflow***

Train a classification model (e.g., Logistic Regression or Random Forest) on the Breast Cancer dataset from scikit-learn.

Save the trained model as a serialized .pkl file.

Serve the model as an API using FastAPI + Uvicorn.

Expose endpoints for real-time predictions via /predict.

Setting up the Lab
1️⃣ Create and Activate Virtual Environment
python3 -m venv fastapi_env
source fastapi_env/bin/activate       # for macOS/Linux
fastapi_env\Scripts\activate          # for Windows

2️⃣ Install Dependencies
pip install -r requirements.txt
