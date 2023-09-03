import datetime
import sqlite3

from discord import Interaction
from app.extentions import clients, cursor, db

@clients.command(name='test')
async def test(ctx):
    await ctx.send("test")
    
@clients.command(name="create_new_event", pass_context=True)
async def create_new_event(ctx, name: str, date):
    cursor.execute("INSERT INTO Main VALUES (?, ?, ?);", (str(ctx.message.author.id), name, str(date),))
    await ctx.send(f"Created Event {name} on {date} by {ctx.message.author.mention}")
    db.commit()
    
#(f"Created Event {name} on {date} by {ctx.user}")