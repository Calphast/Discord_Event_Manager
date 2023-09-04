from sqlalchemy import insert
from app.database.database import user_base, engine


async def input_new_event(server_id, user_id, event_name, event_date):
    smtn = insert(user_base).values(server_id=server_id, user_id=user_id, event_title=event_name, event_date=event_date)
    with engine.connect() as conn:
        try:
            conn.execute(smtn)
            conn.commit()
        except:
            pass