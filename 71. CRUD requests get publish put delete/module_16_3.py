from fastapi import FastAPI, Path

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_users() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def add_user(username: str = Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser"), age: int = Path(ge=18, le=120, description="Enter age", example="24")) -> str:
    max_id_users = str(int(max(users, key=int))+1)
    users[max_id_users] = f"Имя: {username}, возраст: {age}"
    return f"User {max_id_users} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str = Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser"), age: int = Path(ge=18, le=120, description="Enter age", example="24")) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"

@app.delete("/user/{user_id}")
async def delete_user(user_id:str):
    users.pop(user_id)
    return f"User {user_id} has been deleted"
    
