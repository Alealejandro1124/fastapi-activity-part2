# models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id     = Column(Integer, primary_key=True, index=True)
    name   = Column(String(100), nullable=False)
    age    = Column(Integer, nullable=False)
    gender = Column(String(1), nullable=False)

    todos = relationship("Todo", back_populates="user")

class Todo(Base):
    __tablename__ = "todo"
    id        = Column(Integer, primary_key=True, index=True)
    task      = Column(String(256), nullable=False)
    priority  = Column(Integer)
    due_month = Column(String(50))
    due_year  = Column(Integer)

    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user    = relationship("User", back_populates="todos")
