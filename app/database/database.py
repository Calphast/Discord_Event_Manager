from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
from sqlalchemy.ext.asyncio import create_async_engine

engine = create_engine("sqlite:///main.sqlite")

base = declarative_base()

metadata = sqlalchemy.MetaData()

class user_base(base):
    __tablename__='user_base'
    
    server_id = Column(Integer)
    user_id = Column(Integer, primary_key=True)
    event_title = Column(String)
    event_date = Column(String)
    
    def __init__(self, server_id, user_id, event_title, event_date):
        self.server_id = server_id
        self.user_id = user_id
        self.event_title = event_title
        self.event_date = event_date