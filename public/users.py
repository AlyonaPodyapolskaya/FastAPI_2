from fastapi import APIRouter, Body
from models.models import User, User_pwd, Respons, User_contacts
from typing import Union, Annotated

users_router = APIRouter()
#Создание пароля
def create_pwd(cod: str):
    return str(reversed(cod))

list_of_user = [User_pwd(name='Ivan', last_name='Ivanov', age=20, id=105, password='***********')]
list_of_users_contacts = []

def find_user(id: int) -> Union[User_pwd, None]:
    for user in list_of_user:
        if user.id == id:
            return user
    return None

#Получение всех пользователей
@users_router.get("/api/users/", response_model=Union[list[User], None])
def get_users():
    return list_of_user

#Получение одного пользователя
@users_router.get("/api/users/{id}", response_model=Union[User, Respons])
def get_user(id: int):
    user = find_user(id)
    print(user)
    if user == None:
        return Respons(message="Такого пользователя нет")
    return user

#Добавление пользователя
@users_router.post("/api/users/", response_model=Union[User, Respons])
def create_user(item: Annotated[User, Body(embed=True, description="Новый пользователь")]):
    user = User_pwd(name=item.name, last_name=item.last_name, age=item.age, id=item.id, password=create_pwd(item.name))
    list_of_user.append(user)
    return user

#Добавление контактов для пользователя
@users_router.post("/api/users/{id}", response_model=Union[User_contacts, Respons])
def add_contacts(item: Annotated[User_contacts, Body(embed=True, description="Добавления контактов пользователя")]):
    user = find_user(item.id)
    if user == None:
        return Respons(message="Такого пользователя нет")
    users_contacts = User_contacts(id=item.id, user_phone=item.user_phone, user_email=item.user_email)
    list_of_users_contacts.append(users_contacts)
    return users_contacts

#Изменения для пользователя
@users_router.put("/api/users/", response_model=Union[User, Respons])
def edit_user(item: Annotated[User, Body(embed=True, description="Изменение пользователя")]):
    user = find_user(item.id)
    if user == None:
        return Respons(message="Такого пользователя нет")
    user.last_name = item.last_name
    user.name = item.name
    user.age = item.age
    return user

#Удаление пользователя
@users_router.delete("/api/users/{id}", response_model=Union[list[User], Respons])
def delete_user(id: int):
    user = find_user(id)
    if user == None:
        return Respons(message="Такого пользователя нет")
    list_of_user.remove(user)
    return list_of_user