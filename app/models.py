from pydantic import BaseModel
from typing import List

class User(BaseModel):
    username: str
    email: str
    role: str  

class UserInDB(User):
    hashed_password: str
