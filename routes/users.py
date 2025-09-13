from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")

users = {
    1: {"name": "Пользователь 1", "email": "user1@example.com"},
    2: {"name": "Пользователь 2", "email": "user2@example.com"},
    3: {"name": "Пользователь 3", "email": "user3@example.com"},
    4: {"name": "Пользователь 4", "email": "user4@example.com"},
    5: {"name": "Пользователь 5", "email": "user5@example.com"},
}

@router.get("/{user_id}")
def read_user(user_id: int):
    user = users.get(user_id)
    if user:
        return user
    return {"error": "User not found"}

@router.get("/")
def read_users():
    return users