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

@app.get("/subtraction")
async def subtraction(int1: int, int2: int):
    return {"total": int1 - int2}

class Arrow(BaseModel):
    range1: int
    range2: int
@app.post("/Arrow")
async def arrow(input: Arrow):
    return f"The arrow's range is {input.range1} or {input.range2} meters."

class Choice(BaseModel):
    c1: str
    c2: str
@app.post("/choice")
async def choice(input: Choice):
    return f"It is either {input.c1} or {input.c2}."

