import sys
from fastapi import APIRouter, HTTPException

sys.path.append("..")

from services.answerService import AnswerService
from dataClasses.answer import Answer

router = APIRouter()

@router.get("/answers/{task_id}")
def getAnswer(task_id: int, user_id: int):
    answerService = AnswerService()

    answer = answerService.getAnswer(task_id, user_id)
    if answer:
        return answer
    raise HTTPException(404, "Answer not found")

@router.put("/answers/{task_id}")
def putAnswer(task_id: int, answer: Answer): # тут нвдо сперва определиться как ответы выглядят для того, чтобы с ними что-то делать
    answerService = AnswerService()
    if not answerService.saveAnswer(answer.task_id, answer): # либо просто task_id, пока не знаю
        raise HTTPException(409, "Answer already exists")

@router.delete("/answers/{task_id}")
def deleteAnswer(task_id: int, user_id: int):
    answerService = AnswerService()
    if not answerService.deleteAnswer(task_id, user_id):
        raise HTTPException(404, "Answer not found")

@router.patch("/answers/{task_id}")
def updateAnswer(task_id: int, answer: Answer):
    answerService = AnswerService()
    if not answerService.updateAnswer(task_id, answer):
        raise HTTPException(404, "Answer not found")
