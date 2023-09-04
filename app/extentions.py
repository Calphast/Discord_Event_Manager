import sqlite3
from discord import Client, Intents, app_commands
from discord.ext import commands

intents = Intents().all()
intents.message_content = True

clients = Client(
    intents=intents
)

commands = app_commands.CommandTree(client=clients)

#db = sqlite3.connect('main.sqlite')
#cursor = db.cursor()