from fastapi import APIRouter, HTTPException
from schema import UserCreate
from user_store import UserStore

router = APIRouter()
store = UserStore("users.txt")

def get_next_id():
    users = store.load()
    if not users:
        return 1
    return max(user["id"] for user in users) + 1

@router.post("/")
def create_user(user: UserCreate):
    users = store.load()
    new_user = {
        "id": get_next_id(),
        "name": user.name,
        "email": user.email
    }
    users.append(new_user)
    store.save(users)
    return new_user

@router.get("/")
def get_users():
    return store.load()

@router.get("/{user_id}")
def get_user(user_id: int):
    user = store.find_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user