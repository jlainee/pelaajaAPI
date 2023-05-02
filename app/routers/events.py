from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, status, Depends
from models.schemas import EventDb
from models.database import SessionLocal
from models import crud_events

router = APIRouter(prefix='/events')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('', response_model=list[EventDb], status_code=status.HTTP_200_OK)
async def get_events(event_type: str | None = None, db: Session = Depends(get_db)):
    return crud_events.read_events(db, event_type)