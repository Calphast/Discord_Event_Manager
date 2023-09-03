from discord import Client, Intents
from discord.ext import commands

intents = Intents().all()
intents.message_content = True

clients = commands.Bot(
    command_prefix='/',
    intents=intents
)