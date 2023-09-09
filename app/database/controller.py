import os

from sqlalchemy import insert, delete, select, text
from app.database.database import user_base, engine

async def input_new_event(server_id, user_id, event_name, event_date):
    smtn = insert(user_base).values(server_id=server_id, user_id=user_id, event_title=event_name, event_date=event_date)
    with engine.connect() as conn:
        try:
            conn.execute(smtn)
            conn.commit()
        except:
            pass

async def delete_all_events(user_id):
    if(user_id != 776521397211758592):
        return False
    if(user_id == 776521397211758592):
        smtn = delete(user_base)
        with engine.connect() as conn:
            try:
                conn.execute(smtn)
                conn.commit()
            except:
                pass
        return True
    
async def display_events(USER_id):
    smtn = select(user_base.event_title, user_base.event_date).where(user_base.user_id == USER_id)
    with engine.connect() as conn:
        result = conn.execute(smtn)
        result_as_dict = result.mappings().all()
    return result_as_dict