import os
import sqlite3

from app.database import controller
import app.commands
from app.extentions import clients, commands
from app.database.database import engine, base

from dotenv import load_dotenv
load_dotenv(dotenv_path='app\.env')

TOKEN = os.getenv('DISCORD_TOKEN')

@clients.event
async def on_ready():
    print("attempting connection")
    base.metadata.create_all(engine)
    print("connected!")
    print("sync commenced")
    await commands.sync()
    print("sync complete!")
    print(
        f'{clients.user} is online'
    )

def run():
    print("app is now running")
    clients.run(TOKEN)