from fastapi import FastAPI
from app.routes import rolls 
from app.routes import frames
from app.database import engine, Base
from app.models import roll, frame

app = FastAPI()
app.include_router(rolls.router, prefix="/rolls")
app.include_router(frames.router, prefix="/rolls")


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
    print("Tables created!")


@app.get("/")
def root():
    return {"message": "Film Log API"}



