from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from typing import Annotated
from models import User
from schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify


router = APIRouter(prefix="/user", tags=["user"])


@router.get("/")
def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users


@router.get("/{user_id}")
async def user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    # Выбираем пользователя по user_id
    user = db.scalars(select(User).where(User.id == user_id)).first()

    # Если пользователь не найден, выбрасываем исключение
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")

    return user


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(create_data: CreateUser, db: Annotated[Session, Depends(get_db)]):
    # Создаем slug на основе имени пользователя
    create_data_dict = create_data.dict()
    create_data_dict['slug'] = slugify(create_data_dict.get('username', ''))

    # Вставляем нового пользователя в БД
    stmt = insert(User).values(**create_data_dict)
    result = db.execute(stmt)
    db.commit()

    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }


@router.put("/update/{user_id}")
async def update_user(user_id: int, update_data: UpdateUser, db: Annotated[Session, Depends(get_db)]):
    # Обновляем пользователя по user_id
    stmt = update(User).where(User.id == user_id).values(**update_data.dict())
    result = db.execute(stmt)
    db.commit()

    # Если пользователь не найден, выбрасываем исключение
    if result.rowcount == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")

    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'User update is successful!'
    }


@router.delete("/delete/{user_id}")
async def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    # Удаляем пользователя по user_id
    stmt = delete(User).where(User.id == user_id)
    result = db.execute(stmt)
    db.commit()

    # Если пользователь не найден, выбрасываем исключение
    if result.rowcount == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")

    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'User delete is successful!'
    }
