from fastapi import APIRouter, HTTPException
from sqlmodel import select

from dependencies import SessionDep
from models.users import Users
from schema.users import UserOutPut

router = APIRouter()


@router.post("/user/create")
def create_user(user: Users, session: SessionDep) -> str:
    session.add(user)
    session.commit()
    session.refresh(user)
    return "OK"


@router.get('/user/list', response_model=list[UserOutPut])
def user_list(session: SessionDep) -> list[Users]:
    users = session.exec(select(Users)).all()
    return users


@router.get("/user/get", response_model=UserOutPut)
def get_user(user_id: int, session: SessionDep) -> UserOutPut:
    user = session.get(Users, user_id)
    if not user:
        raise HTTPException(detail="user not found", status_code=400)

    return user


@router.delete("/user/delete")
def delete_user(user_id: int, session: SessionDep) -> str:
    user = session.get(Users, user_id)
    if not user:
        raise HTTPException(detail="user not found", status_code=400)

    session.delete(user)
    session.commit()
    return "OK"
