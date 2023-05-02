from sqlalchemy.orm import Session
from . import models, schemas

def read_players(db: Session):
    return db.query(models.Player).all()

def add_player(db: Session, player_in: schemas.PlayerIn):
    player = models.Player(**player_in.dict())
    db.add(player)
    db.commit()
    db.refresh(player)
    return player

def read_player_data(db: Session, user_id: int):
    return db.query(models.Player).filter(models.Player.id == user_id).first()

def create_event(db: Session, user_id: int, event_in: schemas.EventIn):
    event = models.Events(**event_in.dict())
    event.player_id = user_id
    db.add(event)
    db.commit()
    db.refresh(event)
    return event