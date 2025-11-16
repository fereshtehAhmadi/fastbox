from dependencies import SessionDep
from models.users import Users
from fastapi import APIRouter

router = APIRouter()

@router.post("/create/user/")
def create_user(user: Users, session: SessionDep):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
