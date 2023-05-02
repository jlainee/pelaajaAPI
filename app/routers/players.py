from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from models.database import SessionLocal
from models import crud_players

router = APIRouter(prefix='/players')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('')
async def get_players(db: Session = Depends(get_db)):
    return crud_players.read_players(db)