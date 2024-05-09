import pickle 
import re
from pathlib import Path 
import pycaret
from pycaret.classification import *
import pandas as pd
BASE_DIR = Path(__file__).resolve().parent.parent

# with open(f"{BASE_DIR}\\model\\predictive_maintenance.pkl","rb") as f:
#     model = pickle.load(f)

model = load_model(f"{BASE_DIR}\\model\\predictive_maintenance")

classes = {
    0:"gg"
}

def predict_class(input):
    input_df=pd.DataFrame(input)
    predictions = model.predict(input_df)
    print(predictions)
    return predictions.item()


# dummy_data = {
#     'Air temperature [K]': [0.3333333333333286, 0.44444444444444287, 0.22222222222222143, 
#                             0.7777777777777786, 0.3333333333333286, 0.5185455720329861, 0.5401266308704736],
#     'Process temperature [K]': [0.5, 0.5, 0.375, 0.625, 0.375, 0.5104547106713903, 0.7152849194585769],
#     'Rotational speed [rpm]': [0.24039580908032598, 0.3742724097788127, 0.45750873108265433, 
#                                0.11745928319466402, 0.11397964130389841, 0.20133893627883215, 0.2116504717034246],
#     'Torque [Nm]': [0.3698630136986301, 0.2876712328767123, 0.2465753424657534, 0.6301369863013699, 
#                     0.726027397260274, 0.5205679573942655, 0.4261764736619937],
#     'Tool wear [min]': [0.2569169960474308, 0.3043478260869565, 0.1660079051383399, 0.14712147436778086, 
#                         0.8540889831344971, 0.40246624225521516, 0.8326732168616138],
#     'Type_H': [0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0],
#     'Type_L': [0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0],
#     'Type_M': [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]
# }

# dummy_df = pd.DataFrame(dummy_data)
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
# print(predict_class(dummy))
# print(type(model))
