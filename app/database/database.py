from sqlalchemy import Column, Integer, String
import sqlalchemy
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_async_engine("sqlite+aiosqlite:///main.sqlite")

base = sqlalchemy.orm.declarative_base()

class user_base(base):
    __tablename__='user_base'
    
    server_id = Column(Integer)
    user_id = Column(Integer, primary_key=True)
    event_title = Column(String)
    event_date = Column(String)