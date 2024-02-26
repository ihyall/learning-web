import fastapi
from fastapi.middleware.cors import CORSMiddleware

app = fastapi.FastAPI()

origins = ["http://localhost:5500"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    # return "Hello world"
    return fastapi.responses.FileResponse("html/new_graph.html")
