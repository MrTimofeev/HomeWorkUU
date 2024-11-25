from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from typing import Annotated
from models import Task, User
from schemas import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete
from slugify import slugify

router = APIRouter(prefix="/task", tags=["task"])


@router.get("/")
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(Task))
    tasks = result.scalars().all()
    return tasks


@router.get("/{task_id}")
async def task_by_id(task_id: int, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(Task).where(Task.id == task_id))
    task = result.scalars().first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task


@router.post("/create")
async def create_task(task_data: CreateTask, user_id: int, db: Annotated[Session, Depends(get_db)]):
    # Проверяем, существует ли пользователь
    result = db.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")
    
    # Добавляем задачу с привязкой к пользователю
    task_dict = task_data.dict()
    task_dict["user_id"] = user_id  # Устанавливаем связь с пользователем
    task_dict["slug"] = slugify(task_data.title)  # Генерируем slug для задачи
    stmt = insert(Task).values(**task_dict)
    
    try:
        db.execute(stmt)
        db.commit()
        return {"status_code": status.HTTP_201_CREATED, "transaction": "Successful"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.put("/update/{task_id}")
async def update_task(task_id: int, task_data: UpdateTask, db: Annotated[Session, Depends(get_db)]):
    stmt = update(Task).where(Task.id == task_id).values(**task_data.dict(exclude_unset=True))
    result = db.execute(stmt)
    if result.rowcount == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "Task update is successful!"}



@router.delete("/delete/{task_id}")
async def delete_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
    stmt = delete(Task).where(Task.id == task_id)
    result = db.execute(stmt)
    if result.rowcount == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "Task deletion is successful!"}
