import sys
import tomllib
import json

from fastapi import HTTPException

sys.path.append("..")

from services.fileService import FileService
from utils.answer import Answer

def processTaskByIdRequest(id: int):
    with open("config.toml", "rb") as f:
        CONFIG = tomllib.load(f)["tasks"]

    fileService = FileService(CONFIG)
    filename = f"task_{id}.json"


    if fileService.checkIfFileExists(filename):
        taskFile = fileService.getFile(filename)
        taskData = json.load(taskFile)
        taskFile.close()
        return taskData

def saveAnswer(answer: Answer):
    with open("config.toml", "rb") as f:
        CONFIG = tomllib.load(f)["answers"]

    fileService = FileService(CONFIG)
    filename = f"answers_{answer.task_id}.json"

    if not fileService.checkIfFileExists(filename):
        fileService.writeJSON(filename, [])

    data: list[dict] = fileService.readJSON(filename)

    for i, ans in enumerate(data):
        if answer.user_id == ans["user_id"]:
            del data[i]

    answer.date = answer.date.__str__()
    answer.data = answer.data.__dict__
    data.append(answer.__dict__)

    fileService.writeJSON(filename, data)