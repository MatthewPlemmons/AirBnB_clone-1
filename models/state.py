#!/usr/bin/python3
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models import storage


class State(BaseModel, Base):
    """Model for managing state data"""

    def __init__(self, *args, **kwargs):
        super(State, self).__init__(*args, **kwargs)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="delete")
    else:
        name = ""

        @property
        def cities(self):
            city_list = storage.all("City").values()
            return [city for city in city_list if self.id == city.state_id]
