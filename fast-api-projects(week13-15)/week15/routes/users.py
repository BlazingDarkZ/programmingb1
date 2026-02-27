from fastapi import APIRouter, HTTPException
from schema import UserCreate
from user_store import UserStore

router = APIRouter()
store = UserStore("users.db")

@router.post("/")
def create_user(user: UserCreate):
    store.save(user.dict())
    return {"message": "User created successfully"}

@router.get("/")
def get_users():
    return store.load()

@router.get("/{user_id}")
def get_user(user_id: int):
    user = store.find_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user