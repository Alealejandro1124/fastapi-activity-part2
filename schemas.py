# schemas.py
from pydantic import BaseModel
from typing import Optional, List

class UserSchema(BaseModel):
    id: Optional[int] = None
    name: str
    age: int
    gender: str

    class Config:
        orm_mode = True

class TodoBase(BaseModel):
    task: str
    priority: int
    due_month: str
    due_year: int
    user_id: int

class TodoCreate(TodoBase):
    pass

class TodoSchema(TodoBase):
    id: int
    user: UserSchema

    class Config:
        orm_mode = True
