from discord import Client, Intents, app_commands

intents = Intents().all()
intents.message_content = True

clients = Client(
    intents=intents
)

commands = app_commands.CommandTree(client=clients)