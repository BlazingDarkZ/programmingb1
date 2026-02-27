from fastapi import APIRouter, HTTPException
from schema import UserCreate
import json
import os

router = APIRouter()
FILE = "users.txt"

def load_users():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return [json.loads(line) for line in f if line.strip()]

def save_users(users):
    with open(FILE, "w") as f:
        for user in users:
            f.write(json.dumps(user) + "\n")

def get_next_id():
    users = load_users()
    if not users:
        return 1
    return max(user["id"] for user in users) + 1

@router.post("/")
def create_user(user: UserCreate):
    users = load_users()
    new_user = {
        "id": get_next_id(),
        "name": user.name,
        "email": user.email
    }
    users.append(new_user)
    save_users(users)
    return new_user

@router.get("/")
def get_users():
    return load_users()

@router.get("/{user_id}")
def get_user(user_id: int):
    users = load_users()
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")