from sqlalchemy.orm import Session
from . import models

def read_players(db: Session):
    return db.query(models.Player).all()

