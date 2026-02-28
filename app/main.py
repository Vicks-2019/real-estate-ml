from fastapi import FastAPI
from app.schemas import RentRequest
from app.model_loader import load_model
import pandas as pd
import logging
import time
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 🔥 Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO)

model = load_model()

@app.get("/")
def home():
    return {"message": "Real Estate Rent Prediction API is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/predict")
def predict(request: RentRequest):

    start = time.time()

    try:
        df = pd.DataFrame([request.dict()])
        prediction = model.predict(df)

        latency = round(time.time() - start, 4)

        return {
            "prediction": prediction.tolist(),
            "latency": latency
        }

    except Exception as e:
        logging.error(str(e))
        return {"error": str(e)}