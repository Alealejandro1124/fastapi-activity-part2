from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    payload = item.dict()
    payload.update({"item_id": item_id})
    return payload
