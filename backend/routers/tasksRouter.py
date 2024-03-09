import sys
from fastapi import APIRouter, HTTPException

sys.path.append("..")

from controllers.taskController import processTaskByIdRequest, \
    saveAnswer, getAllTasks
from utils.answer import Answer

router = APIRouter()

@router.get("/api")
def getTaskById(id: int):
    task = processTaskByIdRequest(id)
    if task:
        return task
    raise HTTPException(404, "Task not found")

@router.put("/api/save-answer")
def putAnswer(answer: Answer):
    saveAnswer(answer)



@router.get("/api/get-all-tasks")
def getTasks():
    return getAllTasks()