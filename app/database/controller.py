from sqlalchemy import insert, delete, select, update
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
    #checks if it me, this command is solely for experimental purposes
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
    
async def display_events(user_id):
    smtn = select(user_base.event_title, user_base.event_date).where(user_base.user_id == user_id)
    with engine.connect() as conn:
        result = conn.execute(smtn)
        result_as_dict = result.mappings().all()
    return result_as_dict

async def search_for_events(event_name, server_id):
    smtn = select(user_base.event_title, user_base.event_date, user_base.users_attached).where(user_base.event_title == event_name and user_base.server_id == server_id)
    with engine.connect() as conn:
        result = conn.execute(smtn)
        result_as_dict = result.mappings().all()
    return result_as_dict
        
async def add_user_to_event(user_id, event_name, server_id, user_to_add: list):
    smtn = update(user_base).where(user_base.user_id == user_id, user_base.event_title == event_name, user_base.server_id == server_id).values(users_attached=user_to_add)
    with engine.connect() as conn:
        try:
            conn.execute(smtn)
            conn.commit()
        except:
            pass