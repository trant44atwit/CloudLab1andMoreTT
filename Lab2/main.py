from email.header import Header
from typing import Optional

from fastapi import FastAPI, Cookie
from pydantic import BaseModel

app = FastAPI()

@app.get("/headers/")
async def read_items(user_email: Optional[str] = Header(None), my_val: Optional[str] = Header(None)):
    print("Headers received: ")
    print(user_email)
    print(my_val)
    return{"user_email": user_email, "my_val": my_val}

@app.get("/readCookie")
async def read_cookie(username: str = Cookie(None)):
    return {"username": username}
