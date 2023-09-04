import sqlite3
from discord import Client, Intents, app_commands
from discord.ext import commands

intents = Intents().all()
intents.message_content = True

clients = Client(
    intents=intents
)

commands = app_commands.CommandTree(client=clients)

db = sqlite3.connect('main.sqlite')
cursor = db.cursor()

@clients.event
async def database_creation():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS main(
            server_id TEXT,
            user_id TEXT,
            event_title TEXT,
            event_date TEXT
        )
        ''')