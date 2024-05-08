
from fastapi import FastAPI

# from predict import predict_class
# print(FastAPI.__version__)
app =FastAPI()

@app.get("/")
def home():
    return {"health_check":"ok"}

# # @app.post("")
