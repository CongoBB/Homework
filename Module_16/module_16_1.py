from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def main_page():
    return "Главная страница."


@app.get("/user/admin")
async def admin_rights():
    return 'Вы вошли как администратор!'


@app.get("/user/{user_id}")
async def id_getter(user_id):
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user")
async def user_maker(username: str, age: str):
    return f"Информация о пользователе. Имя: {username}, возраст: {age}"
