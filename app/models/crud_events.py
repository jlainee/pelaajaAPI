from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models, schemas

event_types = ["level_started", "level_solved"]

def read_events(db: Session, event_type: str):
    if event_type == None:
        return db.query(models.Events).all()
    elif event_type not in event_types:
        raise HTTPException(
            status_code=400, detail="Invalid event type")
    else: 
        return db.query(models.Events).filter(models.Events.type == event_type).all()
    