from sqlmodel import SQLModel, Field


class Users(SQLModel, table=True):
    id: int = Field(primary_key=True)
    username: str = Field(index=True, unique=True)
    phone_number: str
    password: str
    email: str
