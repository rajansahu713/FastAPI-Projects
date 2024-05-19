from fastapi import HTTPException, status
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Optional
from models import fake_users_db, blocklist_token
from constants import SECRET_KEY, ALGORITHM
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi import Security



class AuthHandler:
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    async def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    async def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    async def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    async def get_user(self, username: str):
        user = next((user for user in fake_users_db if user.username == username), None)
        return user

    async def authenticate_user(self, username: str, password: str):
        user = await self.get_user(username)
        if not user:
            return False
        if not await self.verify_password(password, user.hashed_password):
            return False
        return user
    
    async def blocklist_token(self, token):
        blocklist_token.append(token)

    async def istokenblock(self, token):
        return token in blocklist_token

    
    async def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        token = auth.credentials
        if not token or await self.istokenblock(token):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not authenticated",
                headers={"WWW-Authenticate": "Bearer"},
            )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not authenticated",
                    headers={"WWW-Authenticate": "Bearer"},
                )
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not authenticated",
                headers={"WWW-Authenticate": "Bearer"},
            )
        user = await self.get_user(username)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not authenticated",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return user

