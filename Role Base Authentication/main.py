from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from authentications import get_current_user, authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, get_password_hash
import json
from pydantic import BaseModel
from authorizations import authorize
# Initialize FastAPI app
app = FastAPI()


class User(BaseModel):
    username: str
    password: str


# Define endpoints for token generation and authentication
@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user["username"]}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


# Define a route for registering a new user
@app.post("/register")
async def register_user(user:User):
    hashed_password = get_password_hash(user.password)
    with open('data.json', 'r') as file:
        # Load the existing JSON data into a Python object
        existing_data = json.load(file)
        if user.username in existing_data["users"]:
            return {"message": "User already exists"}
        # Add the new user to the existing data
        existing_data["users"][user.username] = {"username": user.username ,"password": str(hashed_password), "role": "user"}
    with open('data.json', 'w') as file:
        json.dump(existing_data, file, indent=4) 
    return {"message": "User registered successfully"}



@app.get("/check-all")
@authorize(role=['admin','superadmin'])
async def route1(current_user: dict = Depends(get_current_user)):
    return {"message": "This endpoint is accessible to admin and superadmin only"}


@app.get("/check-superadmin")
@authorize(role=['superadmin'])
async def route2(current_user: dict = Depends(get_current_user)):
    return {"message": "This endpoint is accessible to superadmin only"}

