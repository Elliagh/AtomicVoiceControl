from fastapi import FastAPI
from sql_app.database import SessionLocal
from sql_app.models import *
app = FastAPI(
    title="AtomApp"
)


@app.get("/light_on")
def light_on(name:str):
    return SessionLocal.query(Users).all()

CarController =