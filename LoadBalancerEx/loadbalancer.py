import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    environment = os.getenv('APP_NAME', 'localhost')
    hello_message = f"Hello there! Environment: {environment}!"
    return {"hello_message": hello_message}