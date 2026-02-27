from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import json
import os

# -------------------------
# App Initialization
# -------------------------

app = FastAPI(
    title="Final Project - Task Management System",
    description="Backend API for managing tasks using JSON Lines file storage",
    version="1.0.0"
)

# Serve frontend
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/app")
def serve_app():
    return FileResponse("static/index.html")


# -------------------------
# File Handling
# -------------------------

FILE_NAME = "tasks.txt"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    tasks = []
    with open(FILE_NAME, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                tasks.append(json.loads(line))
    return tasks


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(json.dumps(task) + "\n")


# -------------------------
# Models
# -------------------------

class Task(BaseModel):
    id: int
    title: str
    description: str | None = None
    completed: bool = False


class TaskCreate(BaseModel):
    title: str
    description: str | None = None


# -------------------------
# Routes
# IMPORTANT: /stats must come BEFORE /{task_id}
# -------------------------

@app.get("/")
def root():
    return {"message": "Task Management API is running"}


# ---- Get Stats ----

@app.get("/tasks/stats")
def task_stats():
    tasks = load_tasks()

    total = len(tasks)
    completed = len([t for t in tasks if t["completed"]])
    pending = total - completed

    percentage = 0
    if total > 0:
        percentage = (completed / total) * 100

    return {
        "total_tasks": total,
        "completed_tasks": completed,
        "pending_tasks": pending,
        "completion_percentage": percentage
    }


# ---- Get All Tasks (with optional filter) ----

@app.get("/tasks")
def get_tasks(completed: bool | None = None):
    tasks = load_tasks()

    if completed is not None:
        tasks = [task for task in tasks if task["completed"] == completed]

    return tasks


# ---- Get Single Task ----

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")


# ---- Create Task ----

@app.post("/tasks")
def create_task(task: TaskCreate):
    tasks = load_tasks()

    # Safe ID generation
    new_id = max([t["id"] for t in tasks], default=0) + 1

    new_task = {
        "id": new_id,
        "title": task.title,
        "description": task.description,
        "completed": False
    }

    tasks.append(new_task)
    save_tasks(tasks)

    return new_task


# ---- Update Task ----

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    tasks = load_tasks()

    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks[index] = updated_task.dict()
            save_tasks(tasks)
            return updated_task

    raise HTTPException(status_code=404, detail="Task not found")


# ---- Delete Single Task ----

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    tasks = load_tasks()

    new_tasks = [task for task in tasks if task["id"] != task_id]

    if len(new_tasks) == len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")

    save_tasks(new_tasks)
    return {"message": "Task deleted successfully"}


# ---- Delete All Tasks ----

@app.delete("/tasks")
def delete_all_tasks():
    save_tasks([])
    return {"message": "All tasks deleted successfully"}