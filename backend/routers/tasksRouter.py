import sys
from webbrowser import get
from fastapi import APIRouter, HTTPException

sys.path.append("..")

from services.taskService import TaskService
from dataClasses.answer import Answer

router = APIRouter()

@router.get("/tasks/{id}")
def getTaskById(id: int):
    taskService = TaskService()
    task = taskService.getTask(id)
    if task:
        return task
    raise HTTPException(404, "Task not found")

# TODO get, put, delete, patch тут не знаю надо ли это, как будут задачи создаваться


@router.get("/api/get-all-tasks")
def getTasks():
    return getAllTasks()