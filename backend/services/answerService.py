import sys
import tomllib

sys.path.append("..")

from dataClasses.answer import Answer

from .fileService import FileService

class AnswerService():
    def __init__(self):
        with open("config.toml", "rb") as f:
            self.CONFIG = tomllib.load(f)["answers"]
        self.fileService = FileService(self.CONFIG)

    def getAnswerIndex(self, answers: list[dict], user_id: int):
        for i, answer in enumerate(answers):
            if answer["user_id"] == user_id:
                return i

    def getAnswer(self, task_id: int, user_id: int):
        filename = f"answers_{task_id}.json"

        if not self.fileService.checkIfFileExists(filename):
            return False
        
        answers = self.fileService.readJSON(filename)
        idx = self.getAnswerIndex(answers, user_id)
        if idx != None:
            return answers[idx]
        return False

    def saveAnswer(self, task_id, answer: Answer):
        filename = f"answers_{task_id}.json"

        if not self.fileService.checkIfFileExists(filename):
            self.fileService.writeJSON(filename, [])

        answers = self.fileService.readJSON(filename)
        idx = self.getAnswerIndex(answers, answer.user_id)
        if idx != None:
            return False
        else:
            answer.date = answer.date.__str__()
            answer.data = answer.data.__dict__
            answers.append(answer.__dict__)
            self.fileService.writeJSON(filename, answers)
            return True

    def deleteAnswer(self, task_id: int, user_id: int):
        filename = f"answers_{task_id}.json"

        if not self.fileService.checkIfFileExists(filename):
            return False
        
        answers = self.fileService.readJSON(filename)
        idx = self.getAnswerIndex(answers, user_id)
        if idx != None:
            del answers[idx]
            self.fileService.writeJSON(filename, answers)
            return True
        return False

    def updateAnswer(self, task_id: int, answer: Answer):
        filename = f"answers_{task_id}.json"

        if not self.fileService.checkIfFileExists(filename):
            return False
        
        answers = self.fileService.readJSON(filename)
        idx = self.getAnswerIndex(answers, answer.user_id)
        if idx != None:
                answer.date = answer.date.__str__()
                answer.data = answer.data.__dict__
                answers[idx] = answer.__dict__
                self.fileService.writeJSON(filename, answers)
                return True
        else:
            return False
