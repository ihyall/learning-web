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
        return task
    raise HTTPException(404, "Task not found")
