from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    phone_number: str
    email: str

class UserOutPut(UserBase):
    id: int