
from fastapi import FastAPI
from typing import Dict
from pydantic import BaseModel
from app.predict import predict_class
# print(FastAPI.__version__)
app = FastAPI()


class InputData(BaseModel):
    air_temperature: float
    process_temperature: float
    rotational_speed: float
    torque: float
    tool_wear: float
    type_H: float
    type_L: float
    type_M: float

@app.get("/")
def home():
    return {"health_check":"ok"}

@app.post("/predict")
def predict(data: InputData):
    # print(data.data)  # Access the dictionary
    input_dict ={
        "Air temperature [K]": [data.air_temperature],
        "Process temperature [K]": [data.process_temperature],
        "Rotational speed [rpm]":[data.rotational_speed],
        "Torque [Nm]":[data.torque],
        "Tool wear [min]":[data.tool_wear],
        "Type_H":[data.type_H],
        "Type_L":[data.type_L],
        "Type_M":[data.type_M]
    }
    prediction = predict_class(input_dict)  # Extract the dictionary from InputData
    return {"prediction": prediction}
# def predict(data:dict):
#     print(data)
#     prediction = predict_class(data)
#     return {"prediction": prediction}

# dummy = {
# "Air temperature [K]":[0.5401266308704736],
# "Process temperature [K]":[0.7152849194585769],
# "Rotational speed [rpm]":[0.2116504717034246],
# "Torque [Nm]":[0.4261764736619937], 
# "Tool wear [min]":[0.8326732168616138],
# "Type_H":[0.0], 
# "Type_L":[1.0], 
# "Type_M":[0.0],
# }

# print(predict(dummy))
