#!/usr/bin/python3
from models import *
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """Model for storing amenity data"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
