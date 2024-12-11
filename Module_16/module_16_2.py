from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def main_page():
    return "Главная страница."


@app.get("/user/admin")
async def admin_rights():
    return 'Вы вошли как администратор!'


@app.get("/user/{user_id}")
async def id_getter(user_id: int = Path(ge=1, le=100, description="Enter User ID", example="4")):
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user/{username}/{age}")
async def user_maker(username: Annotated
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
    return f"Информация о пользователе. Имя: {username}, возраст: {age}"
