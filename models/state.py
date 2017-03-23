#!/usr/bin/python3
from models import *
from sqlalchemy import *
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Model for managing state data"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    def __init__(self, *args, **kwargs):
        super(State, self).__init__(*args, **kwargs)
