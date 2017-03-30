#!/usr/bin/python3
from models import *
from sqlalchemy import *
from models.base_model import BaseModel, Base


class Review(BaseModel, Base):
    """Model for managing review data"""
    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    text = Column(String(1024), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
