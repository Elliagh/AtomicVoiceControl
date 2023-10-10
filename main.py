from fastapi import FastAPI

app = FastAPI(
    title="AtomApp"
)

@app.get("/")
def hello():
    return "Hello world!"
