from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models, schemas

event_types = ["level_started", "level_solved"]

def player_query(db: Session, user_id: int):
    player = db.query(models.Player).filter(models.Player.id == user_id).first()
    if player is None:
        raise HTTPException(status_code=404, detail=f"Player with id: {user_id} not found")
    return player



def read_players(db: Session):
    return db.query(models.Player).all()

def add_player(db: Session, player_in: schemas.PlayerIn):
    player = models.Player(**player_in.dict())
    db.add(player)
    db.commit()
    db.refresh(player)
    return player

def read_player_data(db: Session, user_id: int):
    return player_query(db, user_id)

def read_player_events(db: Session, user_id: int, event_type: str):
    if event_type not in event_types:
        raise HTTPException(
            status_code=400, detail="Invalid event type")

    player_query(db, user_id)
    
    events = db.query(models.Events).filter(models.Events.player_id == user_id, models.Events.type == event_type).all()
    return events


def create_event(db: Session, user_id: int, event_in: schemas.EventIn):
    player_query(db, user_id)

    event = models.Events(**event_in.dict())
    
    if event.type not in event_types:
        raise HTTPException(
            status_code=400, detail="Invalid event type")
            
    event.player_id = user_id
    db.add(event)
    db.commit()
    db.refresh(event)
    return event