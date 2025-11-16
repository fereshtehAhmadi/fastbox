from fastapi import FastAPI

from routers import users

app = FastAPI(title="FastBox Demo API", version="1.0.0")
app.include_router(users.router, tags=["users"])
