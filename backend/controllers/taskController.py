import sys
import tomllib
import json

from fastapi import HTTPException

sys.path.append("..")

from services.fileService import FileService

def processTaskByIdRequest(id: int):
    # return 1
    with open("config.toml", "r") as f:
        CONFIG = f.read()
        # return CONFIG
        CONFIG = tomllib.loads(CONFIG)

    fileService = FileService(CONFIG["processTaskByIdRequest"])
    filename = f"task{id}.json"


    if fileService.checkIfFileExists(filename):
        taskFile = fileService.getFile(filename)
        taskData = json.load(taskFile)
        taskFile.close()
        return taskData
