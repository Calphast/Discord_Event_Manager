import datetime
import sqlite3

from discord import Interaction
import discord
from app.extentions import clients, commands

@commands.command(name='test')
async def test(ctx: Interaction):
    await ctx.response.send_message("test")
    
#@commands.command(name="create_new_event")
#async def create_new_event(ctx: Interaction, name: str, date: str):
    #cursor.execute("INSERT INTO Main VALUES (?, ?, ?, ?);", (str(ctx.guild_id), str(ctx.user.id), name, date,))
    #await ctx.response.send_message(f"Created Event {name} on {date} by {ctx.user.mention}")
    #db.commit()

#unfinished commands:

'''
@clients.command(name="display_events", pass_context=True)    
async def display_events(ctx):
    await ctx.send("Function not finished")
    
@clients.command(name="clear_all_events", pass_context=True) 
async def clear_all_events(ctx):
    server_owner = clients.get_user(int(ctx.guild.owner.id))
    user_message = clients.get_user(int(ctx.message.author.id))
    if(user_message != server_owner):
        await ctx.send("You are not allowed to use this command!")
    else:
        def check(message: discord.message):
            return message.channel == ctx.channel and message.author 
        await ctx.send("Warning: This will remove all events from this server, are you sure you want to proceed?: ")
        
        cursor.execute("DELETE FROM Main WHERE (server_id = ?);", (str(ctx.message.guild.id),))
        db.commit()
        await ctx.send("Events Cleared")
'''