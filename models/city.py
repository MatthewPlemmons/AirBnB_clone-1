#!/usr/bin/python3
from models import *


class City(BaseModel, Base):
    """Model for storing city data"""
    __tablename__ = "cities"
    state_id = Column(String(60), nullable=False, ForeignKey("states.id")
    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
