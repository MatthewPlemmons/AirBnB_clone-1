#!/usr/bin/python3
from models import *
from sqlalchemy import *
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Model for managing user data"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    places = relationship("Place", cascade="delete", backref="user")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
