from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_all_users():
    return users


@app.get("/user/{user_id}")
async def get_user(user_id: str):
    return users[user_id]


@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int):
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f'Имя: {username}, возраст: {age}'
    return f"User {current_index} has successfully registered."


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str, username: str, age: int):
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"User {user_id} data has been updated"


@app.delete("/user/{user_id}")
async def delete_user(user_id):
    users.pop(user_id)
    return "User has been removed"


@app.delete("/delete")
async def delete_all_users():
    users.clear()
    return "All data has been removed"