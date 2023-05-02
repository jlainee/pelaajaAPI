from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    # events = relationship("events")

class Events(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    detail = Column(String)
    timestamp = Column(DateTime, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S")) # not sure about this
    # player_id = Column(Integer, ForeignKey("players.id"))