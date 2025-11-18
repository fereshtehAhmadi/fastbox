from fastapi import APIRouter, HTTPException
from sqlmodel import select, or_

from dependencies import SessionDep
from models.users import Users
from schema.users import UserOutPut, UserInput, UserUpdate

router = APIRouter()


@router.post("/user/create")
def create_user(user: UserInput, session: SessionDep) -> str:
    valid_user = Users.model_validate(user)
    email_user = session.exec(select(Users).where(
        or_(
                Users.email == user.email,
                Users.username == user.username,
        )
    )
    ).first()
    if email_user:
        raise HTTPException(detail="email and username must be unique!", status_code=400)

    session.add(valid_user)
    session.commit()
    session.refresh(valid_user)
    return "OK"


@router.get('/user/list', response_model=list[UserOutPut])
def user_list(session: SessionDep) -> list[Users]:
    users = session.exec(select(Users)).all()
    return users


@router.get("/user/get/{user_id}", response_model=UserOutPut)
def get_user(user_id: int, session: SessionDep) -> UserOutPut:
    user = session.get(Users, user_id)
    if not user:
        raise HTTPException(detail="user not found", status_code=400)

    return user


@router.delete("/user/delete/{user_id}")
def delete_user(user_id: int, session: SessionDep) -> str:
    user = session.get(Users, user_id)
    if not user:
        raise HTTPException(detail="user not found", status_code=400)

    session.delete(user)
    session.commit()
    return "OK"

@router.patch("/user/update/{user_id}")
def update_user(user_id: int, user: UserUpdate, session: SessionDep) -> str:
    user_instance = session.get(Users, user_id)
    if not user_instance:
        raise HTTPException(detail="user not found", status_code=400)

    user_data = user.model_dump(exclude_unset=True)
    user_instance.sqlmodel_update(user_data)
    session.add(user_instance)
    session.commit()
    session.refresh(user_instance)
    return "OK"
