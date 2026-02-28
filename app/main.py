from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import RentRequest
from app.model_loader import load_model
import pandas as pd
import logging
import time

# -----------------------------
# App Initialization
# -----------------------------

app = FastAPI(title="Real Estate Rent Prediction API")

# -----------------------------
# CORS Configuration
# -----------------------------

origins = [
    "https://real-estate-ml.vercel.app",  # Your Vercel frontend
    "http://localhost:3000",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,  # IMPORTANT: keep False
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Logging Setup
# -----------------------------

logging.basicConfig(level=logging.INFO)

# -----------------------------
# Load ML Model
# -----------------------------

model = load_model()

# -----------------------------
# Routes
# -----------------------------

@app.get("/")
def home():
    return {"message": "Real Estate Rent Prediction API is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/predict")
def predict(request: RentRequest):

    start_time = time.time()

    try:
        # Convert request to DataFrame
        df = pd.DataFrame([request.dict()])

        # Model prediction
        prediction = model.predict(df)

        latency = round(time.time() - start_time, 4)

        return {
            "prediction": prediction.tolist(),
            "latency": latency
        }

    except Exception as e:
        logging.error(f"Prediction error: {str(e)}")
        return {"error": str(e)}