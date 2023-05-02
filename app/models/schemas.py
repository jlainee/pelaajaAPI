from datetime import datetime
from pydantic import BaseModel, Field

class PlayerIn(BaseModel):
    name: str

    class Config:
        orm_mode = True

class PlayerDb(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class EventIn(BaseModel):
    type: str
    detail: str

    class Config:
        orm_mode = True

class EventDb(BaseModel):
    id: int
    type: str
    detail: str
    timestamp: datetime
    player_id: int

    class Config:
        orm_mode = True