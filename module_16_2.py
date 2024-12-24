from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get('/')
async def main_page() -> str:
    return {'message': 'Главная страница'}

@app.get("/user/admin")
async def us_ad() -> str:
    return (f"Вы вошли как администратор")


@app.get("/user/{user_id}")
async def user_id_page(user_id: Annotated[
        int, Path(ge=1, le=100, description='Enter User ID', example=1)]) -> str:
    return (f"Вы вошли как пользователь № {user_id}")

@app.get("/user/{user_name}/{age}")
async def us_age(user_name: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=24)]) -> str:
    return (f"Информация о пользователе. Имя: {user_name}, Возраст: {age}")
