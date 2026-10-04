from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"Hello": "World"}


@app.get('/about')
def about():
    return {"About": "This is a simple FastAPI application."}   
