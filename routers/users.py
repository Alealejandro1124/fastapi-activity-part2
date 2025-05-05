# routers/users.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import User, Todo
from schemas import UserSchema, TodoSchema

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=List[UserSchema])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.post("/", response_model=UserSchema)
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    db_user = User(**user.dict(exclude={"id"}))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/count", summary="Get total user count", tags=["Aggregations"])
def get_user_count(db: Session = Depends(get_db)):
    return {"user_count": db.query(func.count(User.id)).scalar()}

@router.get("/todo_by_month", response_model=List[TodoSchema], tags=["Joins"])
def get_user_todo_by_month(user_name: str, month: str, db: Session = Depends(get_db)):
    return (
        db.query(Todo)
          .join(User)
          .filter(User.name == user_name, Todo.due_month == month)
          .all()
    )

@router.get("/by_todo", tags=["Joins"])
def get_user_by_todo(keyword: str, db: Session = Depends(get_db)):
    rows = (
        db.query(User.name)
          .join(Todo)
          .filter(Todo.task.like(f"%{keyword}%"))
          .all()
    )
    return [r[0] for r in rows]
