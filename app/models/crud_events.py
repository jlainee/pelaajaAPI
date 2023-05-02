from sqlalchemy.orm import Session
from . import models, schemas

def read_events(db: Session, event_type: str):
    if event_type == None:
        return db.query(models.Events).all()
    else: 
        return db.query(models.Events).filter(models.Events.type == event_type).all()
    