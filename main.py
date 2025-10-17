from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, constr
from sqlmodel import SQLModel, Field, Session, create_engine
from typing import Annotated

app = FastAPI(title="FastBox Demo API", version="1.0.0")


class Users(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    phone_number: str
    password: str


sqlite_file_name = "fastbox.sqlite"
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


class UserCreate(BaseModel):
    username: str
    phone_number: constr(pattern=r"^09\d{9}$")
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    phone_number: str

    class Config:
        orm_mode = True


@app.post("/create/user/", response_model=UserOut)
def create_user(user: UserCreate, session: SessionDep):
    existing_user = session.query(Users).filter(Users.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    db_user = Users(**user.dict())
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user
