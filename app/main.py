from fastapi import FastAPI
from routers import players, events 
from models.database import engine
from models import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(players.router)
app.include_router(events.router)