from sqlmodel import SQLModel, Field


class Users(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    username: str = Field(index=True, unique=True)
    phone_number: str
    password: str
    email: str
