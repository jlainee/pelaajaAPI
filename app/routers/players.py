from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, status, Depends
from models.schemas import PlayerIn, PlayerDb
from models.database import SessionLocal
from models import crud_players

router = APIRouter(prefix='/players')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('', response_model=list[PlayerDb])
async def get_players(db: Session = Depends(get_db)):
    return crud_players.read_players(db)

@router.post('', response_model=PlayerDb, status_code=status.HTTP_201_CREATED)
def add_player(player_in: PlayerIn, db: Session = Depends(get_db)):
    return crud_players.add_player(db, player_in)

