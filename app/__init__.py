import os
import sqlite3

import app.commands
from app.extentions import clients

from dotenv import load_dotenv
load_dotenv(dotenv_path='app\.env')

TOKEN = os.getenv('DISCORD_TOKEN')

@clients.event
async def on_ready():
    print("sync commenced")
    await clients.tree.sync()
    print(f"sync complete")
    print(
        f'{clients.user} is online'
    )

def run():
    print("app is now running")
    clients.run(TOKEN)