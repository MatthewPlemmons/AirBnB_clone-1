#!/usr/bin/python3
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import *
from models.base_model import BaseModel, Base


class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
            "mysql://{}:{}@{}/{}".format(
                getenv("HBNB_MYSQL_USER"),
                getenv("HBNB_MYSQL_PWD"),
                getenv("HBNB_MYSQL_HOST"),
                getenv("HBNB_MYSQL_DB")))

        if getenv("HBNB_MYSQL_ENV", None) == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        classes = {"Amenity": Amenity, "City": City, "Place": Place,
                   "Review": Review, "State": State, "User": User}
        objs = {}
        if cls:
            for obj in self.__session.query(classes[cls]):
                objs[obj.id] = obj
        else:
            for c in classes:
                for obj in self.__session.query(classes[c]):
                    objs[obj.id] = obj
        return objs

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine))

    def close(self):
        self.__session.remove()
