from fastapi import FastAPI

app = FastAPI()


# Root Endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to FastAPI!"
    }


# Path Parameter Endpoint
@app.get("/greet/{name}")
def greet(name: str):
    return {
        "message": f"Hello, {name}!"
    }