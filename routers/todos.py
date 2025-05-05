# routers/todos.py
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import Todo
from schemas import TodoCreate, TodoSchema

router = APIRouter(prefix="/todos", tags=["Todos"])

@router.post("/", response_model=TodoSchema)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@router.get("/", response_model=List[TodoSchema])
def read_todos(db: Session = Depends(get_db)):
    return db.query(Todo).all()

@router.get("/{todo_id}", response_model=TodoSchema)
def read_one_todo(todo_id: int, db: Session = Depends(get_db)):
    t = db.query(Todo).filter(Todo.id == todo_id).first()
    if not t:
        raise HTTPException(404, "Todo not found")
    return t

@router.put("/{todo_id}", response_model=TodoSchema)
def update_todo(todo_id: int, todo: TodoCreate, db: Session = Depends(get_db)):
    qs = db.query(Todo).filter(Todo.id == todo_id)
    if not qs.first():
        raise HTTPException(404, "Todo not found")
    qs.update(todo.dict(), synchronize_session=False)
    db.commit()
    return qs.first()

@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    qs = db.query(Todo).filter(Todo.id == todo_id)
    if not qs.first():
        raise HTTPException(404, "Todo not found")
    qs.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
