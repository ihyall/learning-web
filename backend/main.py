from fastapi import FastAPI
from routers import tasksRouter, answersRouter


app = FastAPI()

app.include_router(tasksRouter.router)
app.include_router(answersRouter.router)
