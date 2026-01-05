from fastapi import FastAPI
from app.features import hash_feature
from app.model import predict

app = FastAPI()

@app.get("/predict")
def predict_endpoint(user_id: str):
    feature = hash_feature(user_id)
    result = predict(feature)
    return {"prediction": result}
