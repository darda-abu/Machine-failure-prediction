FROM python:3.11.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app

EXPOSE 8000

# 
# CMD ["fastapi", "run", "app/main.py", "--port", "80"]

CMD ["uvicorn", "app.main:app", "--reload"]
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

# COPY ./requirements.txt /app/requirements.txt

# RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# COPY ./app /app/app