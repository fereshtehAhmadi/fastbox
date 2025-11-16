from fastapi import FastAPI, HTTPException

from database import SessionDep
from models import Users

app = FastAPI(title="FastBox Demo API", version="1.0.0")


@app.post("/create/user/")
def create_user(user: Users, session: SessionDep):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
