from pydantic import BaseModel
from typing import List

class User(BaseModel):
    username: str
    email: str
    hashed_password: str

# In-memory "database"
fake_users_db: List[User] = []
blocklist_token =[]
