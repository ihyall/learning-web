import sys
from fastapi import APIRouter, HTTPException
import asyncio
import os

sys.path.append("..")

from controllers.taskController import processTaskByIdRequest

router = APIRouter()

@router.get("/api")
def getTaskById(id: int):
    task = processTaskByIdRequest(id)
    if task:
        # return 123
        return task
        # return asyncio.run(task)
        # return os.listdir()
    raise HTTPException(404, "Task not found")
