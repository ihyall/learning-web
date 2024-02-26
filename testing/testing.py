import fastapi
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = fastapi.FastAPI()
# app.mount("/button", StaticFiles(directory="button"), name="static")

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def hello():
    return "Hello World"

# @app.get("/button")
# def button():
#     return fastapi.responses.FileResponse("button/button.html")
