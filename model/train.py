import pandas as pd
import joblib
from xgboost import XGBRegressor
import os

# Load raw data
data_path = os.path.join("data", "raw", "real_estate.csv")
df = pd.read_csv(data_path)

X = df.drop("annual_rent", axis=1)
y = df["annual_rent"]

model = XGBRegressor(n_estimators=200, max_depth=5)
model.fit(X, y)

# Save model
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/model.joblib")

print("Model trained and saved successfully.")