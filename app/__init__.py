import os

from .database import controller
import .commands
from .extentions import clients, commands
from .database.database import engine, base
from .database.migrate import Migration

from dotenv import load_dotenv
load_dotenv(dotenv_path='app\.env')

TOKEN = os.getenv('DISCORD_TOKEN')

@clients.event
async def on_ready():
    print("command sync commenced")
    await commands.sync()
    print("sync complete!")
    print(
        f'{clients.user} is online'
    )

def run():
    print("attempting db connection")
    
    base.metadata.create_all(engine)
    Migration.cfg.set_main_option('sqlalchemy.url', database_uri)
    Migration.cfg.config_file_name = 'alembic.ini'
    if not path.exists('migrations'):
        Migration.init() 
    
    if not Migration.check():
        Migration.revision()
        Migration.upgrade()
        
    print("db connected!")
    print("app is now running")
    clients.run(TOKEN)
