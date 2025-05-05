# main.py
from fastapi import FastAPI
from routers.todos import router as todos_router
from routers.users import router as users_router

app = FastAPI()

app.include_router(todos_router)
app.include_router(users_router)
