from fastapi import FastAPI
from routes import users

app = FastAPI(title="Week 13 API")

app.include_router(users.router, prefix="/users")

@app.get("/")
def root():
    return {"message": "Week 13 running"}