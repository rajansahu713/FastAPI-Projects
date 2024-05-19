from fastapi import FastAPI, Depends
from controller import auth_router
from models import User
from auth import AuthHandler

app = FastAPI()
auth_handler = AuthHandler()

app.include_router(auth_router, prefix="/auth", tags=["Auth"])

@app.get("/auth-test")
async def read_users_me(current_user: User = Depends(auth_handler.auth_wrapper)):
    return current_user

