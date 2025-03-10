from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from .models import User
from .auth import get_current_user
from .utils import create_access_token

app = FastAPI()


@app.post("/token")
def login(user: User):
    
    token = create_access_token(data={"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}


@app.get("/admin")
async def read_admin(user: User = Depends(get_current_user)):
    if user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have access to this resource"
        )
    return {"message": f"Hello, admin {user.username}!"}


@app.get("/operator")
async def read_operator(user: User = Depends(get_current_user)):
    if user.role != "operator":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have access to this resource"
        )
    return {"message": f"Hello, operator {user.username}!"}


@app.get("/viewer")
async def read_viewer(user: User = Depends(get_current_user)):
    if user.role != "viewer":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have access to this resource"
        )
    return {"message": f"Hello, viewer {user.username}!"}
