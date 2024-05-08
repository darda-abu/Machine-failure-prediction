import pickle 
import re
from pathlib import Path 
import pycaret
from pycaret.classification import *
import pandas as pd
BASE_DIR = Path(__file__).resolve().parent.parent

with open(f"{BASE_DIR}\\model\\predictive_maintenance.pkl","rb") as f:
    model = pickle.load(f)



classes = {
    0:"gg"
}

def predict_class(input):
    input_df=pd.DataFrame(input)
    predictions = predict_model(model, data=input_df)
    return predictions
