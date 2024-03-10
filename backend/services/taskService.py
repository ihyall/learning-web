import sys
import tomllib

sys.path.append("..")

from .fileService import FileService

class TaskService():
    def __init__(self):
        with open("config.toml", "rb") as f:
            self.CONFIG = tomllib.load(f)["tasks"]
        self.fileService = FileService(self.CONFIG)


    def getTask(self, id: int):
        filename = f"task_{id}.json"

        if self.fileService.checkIfFileExists(filename):
            taskData = self.fileService.readJSON(filename)
            return taskData
