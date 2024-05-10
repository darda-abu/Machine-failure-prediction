import pickle 
import re
from pathlib import Path 
import pycaret
from pycaret.classification import *
import pandas as pd
import joblib
import json 
import numpy as np
BASE_DIR = Path(__file__).resolve().parent.parent

model = load_model(f"{BASE_DIR}/model/predictive_maintenance")

def get_label(label):
    with open(f"{BASE_DIR}/data/label_mapping.json", 'r') as f:
        label_mapping = json.load(f)
    return {v: k for k, v in label_mapping.items()}[label]

features = open(f"{BASE_DIR}/data/columns.txt", "r").read().split(',')

def process(input_df):
    input_df_encoded = pd.get_dummies(input_df, columns=['Type']).astype('int')
    missing_cols = set(['Type_H', 'Type_M', 'Type_L']) - set(input_df_encoded.columns)
    for col in missing_cols:
        input_df_encoded[col] = 0
    input_df_encoded = input_df_encoded[features]
    scaler = joblib.load(f"{BASE_DIR}/data/scaler.pkl")
    input_df_encoded = scaler.transform(input_df_encoded)
    input_df_encoded = pd.DataFrame(input_df_encoded, columns=features)
    return input_df_encoded
    

def predict_class(input):
    input_df=pd.DataFrame(input)
    input_df_encoded = process(input_df)
    print(input_df_encoded)
    predictions = model.predict(input_df_encoded)
    return predictions.item()


























# dick = {
#     "Air temperature [K]": [298.9],
#     "Process temperature [K]": [309.2],
#     "Rotational speed [rpm]": [1412],
#     "Torque [Nm]": [44.1],
#     "Tool wear [min]": [140],
#     "Type": ["M"]
# }

# print(predict_class(dick))


# ['Air temperature [K]',
#   'Process temperature [K]',
#   'Rotational speed [rpm]',
#   'Torque [Nm]', 'Tool wear [min]',
#   'Type_H', 'Type_L', 'Type_M']
    