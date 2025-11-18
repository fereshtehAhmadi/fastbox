from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    phone_number: str
    email: str


class UserInput(UserBase):
    password: str


class UserOutPut(UserBase):
    id: int


class UserUpdate(BaseModel):
    username: str | None = None
    phone_number: str | None = None
    email: str | None = None
