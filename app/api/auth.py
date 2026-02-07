from fastapi import APIRouter
from app.core.security import create_access_token

router = APIRouter()

@router.post("/login")
def login(email: str):
    # MVP: fake user
    token = create_access_token({"sub": email, "role": "explore"})
    return {"access_token": token, "token_type": "bearer"}
