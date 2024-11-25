from fastapi import FastAPI
from routers import task, user
from sqlalchemy.schema import CreateTable
from backend.db import engine, Base
from models.task import Task
from models.user import User


# Создаем таблицы в базе данных
Base.metadata.create_all(bind=engine)

# Выводим SQL запросы для создания таблиц
# print(CreateTable(User.__table__).compile(engine))
# print(CreateTable(Task.__table__).compile(engine))


app = FastAPI()


@app.get("/")
def home_page() -> dict:
    return {"message": "Welcome to Taskmanager"}


app.include_router(task.router)
app.include_router(user.router)
