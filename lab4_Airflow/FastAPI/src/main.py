from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel, create_model
from predict import predict_data  # make sure you import predict_bc.py
from sklearn.datasets import load_breast_cancer

# Load dataset metadata for feature names
bc = load_breast_cancer()
FEATURE_NAMES = bc.feature_names

app = FastAPI()

# Dynamically build Pydantic model with proper annotations
CancerData = create_model(
    "CancerData",
    **{name.replace(" ", "_"): (float, ...) for name in FEATURE_NAMES}
)

class CancerResponse(BaseModel):
    result: str  # malignant or benign

@app.get("/", status_code=status.HTTP_200_OK)
async def health_ping():
    return {"status": "ready for predictions"}

@app.post("/predict", response_model=CancerResponse)
async def predict_cancer(features: CancerData):
    try:
        X = [[getattr(features, f.replace(" ", "_")) for f in FEATURE_NAMES]]
        prediction = predict_data(X)
        label = "malignant" if prediction[0] == 0 else "benign"
        return CancerResponse(result=label)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
