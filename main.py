from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root_route():
    return {"message": "Hello from the Cloud!"}

@app.get("/greetings")
async def greetings(name: str, age: int):
    return f"Greetings {name}, good to know you are {age} years old."

@app.get("/salutations/{name}/{age}")
async def salutations_path(name: str, age: int):
    return f"Salutations {name}, you are {age} years old."

class PersonInput(BaseModel):
    name: str
    age: int
@app.post("/Yoda_personclass")
async def Yoda_personclass(input: PersonInput):
    return f"{input.age} years you are, young {input.name}"

@app.get("/time")
async def time():
    return {"time": datetime.now().strftime("%I:%M:%S")}

@app.get("/date")
async def date():
    return {"date": datetime.now().strftime("%m/%d/%Y")}

@app.get("/addition")
async def addition(int1: int, int2: int):
    return {"total": int1 + int2}