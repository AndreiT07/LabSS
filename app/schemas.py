from pydantic import BaseModel, EmailStr
from enum import Enum

class RoleEnum(str, Enum):
    admin = "admin"
    operator = "operator"
    viewer = "viewer"

class User(BaseModel):
    username: str
    email: EmailStr
    role: RoleEnum

class UserCreate(User):
    password: str
