from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy

engine = create_engine("sqlite:///main.sqlite")

base = declarative_base()

metadata = sqlalchemy.MetaData()

class user_base(base):
    __tablename__='user_base'
    
    server_id = Column(Integer)
    user_id = Column(Integer)
    event_title = Column(String, primary_key=True)
    event_date = Column(String)
    users_attached = Column(String, nullable=True)
    
    def __init__(self, server_id, user_id, event_title, event_date):
        self.server_id = server_id
        self.user_id = user_id
        self.event_title = event_title
        self.event_date = event_date
