from fastapi import FastAPI

app = FastAPI(
    title="AtomApp"
)

@app.get("/")
def hello():
    return "Hello world!"


@app.get("/light_on")
def light_on(name:str):
    return name