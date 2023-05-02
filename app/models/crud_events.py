from sqlalchemy.orm import Session
from . import models, schemas

def read_events(db: Session):
    return db.query(models.Events).all()