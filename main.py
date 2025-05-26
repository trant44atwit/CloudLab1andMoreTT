from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root_route():
    return {"message": "Hello from FastAPI"}

@app.get("/hello")
async def hello(name: str, age: int):
    return f"Hello {name}, you are {age} years old"

@app.get("/hello_path/{name}/{age}")
async def hello_path(name: str, age: int):
    return f"Hello {name}, you are {age} years old"

class PersonInput(BaseModel):
    name: str
    age: int
@app.post("/hello_personclass")
async def hello_personclass(input: PersonInput):
    return f"Hello {input.name}, you are {input.age} years old"
