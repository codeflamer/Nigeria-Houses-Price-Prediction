from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import util as util

util.load_artifacts()

app = FastAPI()

class PredictionRequest(BaseModel):
    bedrooms: int
    bathrooms: int
    toilets: int
    parking_space: int
    title: str
    town: str
    state: str

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/predict")
def predict(data: PredictionRequest):
    price = util.get_price_prediction(data.bedrooms, data.bathrooms, data.toilets, data.parking_space, data.title, data.town, data.state)
    return {"price": price}

if __name__ == "__main__":
    # uvicorn.run(app, host="0.0.0.0", port=8000)
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
