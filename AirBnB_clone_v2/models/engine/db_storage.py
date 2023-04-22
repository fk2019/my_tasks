#!/usr/bin/enb python3
"""DBStorage engine uses MySQL db
"""
from os import getenv
from sqlalchemy import (create_engine)
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State
from models.amenity import Amenity

database = getenv("HBNB_MYSQL_DB")
user = getenv("HBNB_MYSQL_USER")
host = getenv("HBNB_MYSQL_HOST")
pwd = getenv("HBNB_MYSQL_PWD")
env = getenv("HBNB_ENV")

classes = {"City": City, "Place": Place, "Review": Review,
           "User": User, "State": State, "Amenity": Amenity}


class DBStorage():
    """DBStorage class linkes with MySQL database
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the engine"""
        self.__engine = create_engine('mysql+mysqld://{}.{}@{}/{}'.format
                                      (user, pwd, host, database),
                                      pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query current db session all objects depending on cls"""
        db_objs = {}
        if cls == None:
            for k, v in classes.items():
                for obj in self.__session.query(v).all():
                    key = str(v.__name__) + '.' + str(obj.id)
                    value = obj
                    db_objs[key] = value
        else:
            if type(cls) is str and cls in classes:
                for obj in self.__session.query(classes[cls]).all():
                    key = obj.__class__.__name__ = + '.' + str(obj.id)
                    value = obj
                    db_objs[key] = value
            elif cls.__name__ in classes:
                print(f"cls = {cls}")
                for obj in self.__session.query(cls).all():
                    print(f"obj = {obj}")
                    key = obj.__class__.__name__ = + '.' + str(obj.id)
                    value = obj
                    db_objs[key] = value
        return db_objs

    def new(self, obj):
        """Add object to current db session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes of current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from currrent db session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in db
           Create current db session from the engine by using sessionmaker
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Terminate current db session"""
        self.__session.close()
