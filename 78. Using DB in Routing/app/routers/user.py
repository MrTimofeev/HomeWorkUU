from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from typing import Annotated
from models import User, Task
from schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify


router = APIRouter(prefix="/user", tags=["user"])


@router.get("/")
async def all_users(db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(User))
    users = result.scalars().all()
    return users


@router.get("/{user_id}")
async def user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")
    return user


@router.get("/{user_id}/tasks")
async def tasks_by_user_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    # Проверяем, существует ли пользователь
    user_result = db.execute(select(User).where(User.id == user_id))
    user = user_result.scalars().first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")

    # Получаем задачи пользователя
    tasks_result = db.execute(select(Task).where(Task.user_id == user_id))
    tasks = tasks_result.scalars().all()
    return tasks


@router.post("/create")
async def create_user(user_data: CreateUser, db: Annotated[Session, Depends(get_db)]):
    user_dict = user_data.dict()
    # Создаем slug на основе имени пользователя
    user_dict["slug"] = slugify(user_data.username)
    stmt = insert(User).values(**user_dict)
    try:
        db.execute(stmt)
        db.commit()
        return {"status_code": status.HTTP_201_CREATED, "transaction": "Successful"}
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.put("/update/{user_id}")
async def update_user(user_id: int, user_data: UpdateUser, db: Annotated[Session, Depends(get_db)]):
    stmt = update(User).where(User.id == user_id).values(**user_data.dict(exclude_unset=True))
    result = db.execute(stmt)
    if result.rowcount == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "User update is successful!"}


@router.delete("/delete/{user_id}")
async def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    # Удаляем задачи пользователя
    delete_tasks_stmt = delete(Task).where(Task.user_id == user_id)
    db.execute(delete_tasks_stmt)

    # Удаляем пользователя
    delete_user_stmt = delete(User).where(User.id == user_id)
    result = db.execute(delete_user_stmt)
    if result.rowcount == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")

    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "User and related tasks deleted successfully!"}
