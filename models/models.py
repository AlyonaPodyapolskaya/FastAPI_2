from pydantic import BaseModel, Field
from typing import Union, Annotated

class User(BaseModel):
    name: Union[str, None] = None
    last_name: Union[str, None] = None
    age: Union[int, None] = None
    id: Annotated[Union[int, None], Field(default=100, ge=1, lt=200)] = None

class User_contacts(BaseModel):
    id: Annotated[Union[int, None], Field(default=100, ge=1, lt=200)] = None
    user_phone: Union[str, None] = None
    user_email: Union[str, None] = None

class User_pwd(User):
    password: Annotated[Union[str, None], Field(max_length=200, min_length=3)] = None

class Respons(BaseModel):
    message: str