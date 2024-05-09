
from fastapi import FastAPI
from typing import Dict
from pydantic import BaseModel
from app.predict import predict_class, get_label
app = FastAPI()


class InputData(BaseModel):
    air_temperature: float
    process_temperature: float
    rotational_speed: float
    torque: float
    tool_wear: float
    type: str

@app.get("/")
def home():
    return {"health_check":"ok"}


@app.post("/predict")
def predict(data: InputData):
    input_dict ={
        "Air temperature [K]": [data.air_temperature],
        "Process temperature [K]": [data.process_temperature],
        "Rotational speed [rpm]":[data.rotational_speed],
        "Torque [Nm]":[data.torque],
        "Tool wear [min]":[data.tool_wear],
        "Type":[data.type]
    
    }

    prediction = predict_class(input_dict)
    predicted_label = get_label(prediction)  # Extract the dictionary from InputData
    return {"prediction": predicted_label}

