from fastapi import FastAPI
import json

app = FastAPI()

def load_Data():
    with open('patient.json', 'r') as file:
        data = json.load(file)
    return data

@app.get("/")
def hello():
    return {"Hello": "World"}


@app.get('/about')
def about():
    return {"About": "This is a simple FastAPI application."}   

@app.get('/view')
def view():
    data = load_Data()
    return data