import sqlite3
from discord import Client, Intents
from discord.ext import commands

intents = Intents().all()
intents.message_content = True

clients = commands.Bot(
    command_prefix='/',
    intents=intents
)

db = sqlite3.connect('main.sqlite')
cursor = db.cursor()

@clients.event
async def database_creation():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS main(
            user_id TEXT,
            event_title TEXT,
            event_date TEXT
        )
        ''')