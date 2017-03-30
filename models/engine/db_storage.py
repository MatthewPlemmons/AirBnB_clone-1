from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import *


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
        classes = ["Amenity", "City", "Place", "Review", "State", "User"]
        objs = {}
        if cls in classes:
            for obj in self.__session.query(cls):
                objs[obj.id] = obj
        else:
            for c in classes:
                for obj in self.__session.query(c):
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
