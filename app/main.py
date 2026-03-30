from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

# Load model
with open("app/model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def home():
    return {"message": "ML API Running "}

@app.post("/predict")
def predict(data: dict):
    try:
        features = np.array(data["features"]).reshape(1, -1)
        prediction = model.predict(features)

        return {
            "prediction": prediction.tolist()
        }
    except Exception as e:
        return {"error": str(e)}