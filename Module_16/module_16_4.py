from fastapi import FastAPI, Path, status, Body, HTTPException
from typing import Annotated
from typing import List
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/users")
async def get_all_users()-> List[User]:
    return users


@app.get("/user/{user_id}")
async def get_user(user_id: int = Path(ge=1, le=100, description="Enter User ID", example="4"))-> User:
    try:
        return users[user_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.post("/user/{username}/{age}")
async def create_user(user: User, username: Annotated
[
    str,
    Path(
        min_length=5,
        max_length=20,
        description="Enter username",
        example="Pudge"
    )
],
                     age: int = Path(ge=18, le=120, description="Enter age", example='99'))-> str:
    current_index = len(users) + 1
    user.id = current_index
    user.username = username
    user.age = age
    users.append(user)
    return f"User {user} has successfully registered."


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: Annotated
[
    str,
    Path(
        min_length=5,
        max_length=20,
        description="Enter username",
        example="Pudge"
    )
],
                     age: int = Path(ge=18, le=120, description="Enter age", example='99')):
    try:
        edit_user = users[user_id-1]
        edit_user.username = username
        edit_user.age = age
        return f"User {users[user_id-1]} data has been updated"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
    try:
        deleted_user = users.pop(user_id-1)
        return f"User {deleted_user} has been removed"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/delete")
async def delete_all_users():
    users.clear()
    return "All data has been removed"
