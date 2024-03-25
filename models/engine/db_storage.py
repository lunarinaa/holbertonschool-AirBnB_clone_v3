import os
import sys

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from models.base_model import Base, BaseModel

load_dotenv()

USER = os.environ['HBNB_MYSQL_USER']
PASSWORD = os.environ['HBNB_MYSQL_PWD']
HOST = os.environ['HBNB_MYSQL_HOST']
DB = os.environ['HBNB_MYSQL_DB']


class DBStorage:
    __engine = None
    __session = None
    
    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(USER, PASSWORD,
                                              HOST, DB),
                                      pool_pre_ping=True)
        if 'test' in sys.argv:
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        session = self.__session
        
        result = {}
        
        if cls:
            result[cls.__name__ + '.' + cls.id] = session.query(cls).all()
            return result
        else:
            for c in BaseModel.__subclasses__():
                result[c.__name__ + '.' + c.id] = session.query(c).all()
            return result
    
    def new(self, obj):
        self.__session.add(obj)
    
    def save(self):
        self.__session.commit()
    
    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)
    
    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
    
    def close(self):
        self.__session.close()