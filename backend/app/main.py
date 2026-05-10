from fastapi import FastAPI
from app.database import engine

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Film Log API"}


@app.on_event("startup")
def startup():
    print("Connecting to database...")
    engine.connect()
    print("Database connected!")