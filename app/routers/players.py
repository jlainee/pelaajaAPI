from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, status, Depends
from models.schemas import PlayerIn, PlayerBase, PlayerDb, EventIn
from models.database import SessionLocal
from models import crud_players

router = APIRouter(prefix='/players')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('', response_model=list[PlayerBase], status_code=status.HTTP_200_OK)
async def get_players(db: Session = Depends(get_db)):
    return crud_players.read_players(db)

@router.post('', response_model=PlayerBase, status_code=status.HTTP_201_CREATED)
def add_player(player_in: PlayerIn, db: Session = Depends(get_db)):
    return crud_players.add_player(db, player_in)

@router.get('/{id}', response_model=PlayerDb, status_code=status.HTTP_200_OK)
def get_player_data(id: int, db: Session = Depends(get_db)):
    return crud_players.read_player_data(db, id)

@router.get('/{id}/events', status_code=status.HTTP_200_OK)
def get_player_events(id: int, event_type: str, db: Session = Depends(get_db)):
    return crud_players.read_player_events(db, id, event_type)

@router.post('/{id}/events', status_code=status.HTTP_201_CREATED)
def create_event(id: int, event_in: EventIn, db: Session = Depends(get_db)):
    return crud_players.create_event(db, id, event_in)
