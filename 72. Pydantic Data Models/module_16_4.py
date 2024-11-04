from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/users")
async def get_users() -> list:
    return users


@app.post("/user/{username}/{age}")
async def add_user(username: str = Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser"), age: int = Path(ge=18, le=120, description="Enter age", example="24")) -> User:
    if len(users) == 0:
        user = User(
            id=1,
            username=username,
            age=age
        )
    else:
        user = User(
            id=max(user.id for user in users)+1,
            username=username,
            age=age
        )
    users.append(user)
    return user


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str = Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser"), age: int = Path(ge=18, le=120, description="Enter age", example="24")) -> User:
    for i in users:
        if i.id == user_id:
            i.username = username
            i.age = age
            return i
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> User:
    for i in users:
        if i.id == user_id:
            users.remove(i)
            return i

    raise HTTPException(status_code=404, detail="User was not found")
