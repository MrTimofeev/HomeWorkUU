from backend.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)  # целое число, первичный ключ, с индексом
    username = Column(String)  # строка
    firstname = Column(String)  # строка
    lastname = Column(String)  # строка
    age = Column(Integer)  # целое число
    slug = Column(String, unique=True, index=True)  # строка, уникальная, с индексом

    # Объект связи с таблицей Task, где back_populates='user'
    tasks = relationship("Task", back_populates="user")