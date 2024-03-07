from fastapi import FastAPI
from routers import tasksRouter


app = FastAPI()

app.include_router(tasksRouter.router)

@app.get("/")
def root():
    return "Hello world"
