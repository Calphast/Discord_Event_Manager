from .database.controller import input_new_event

from discord import Interaction
from .extentions import clients, commands

@commands.command(name='test')
async def test(ctx: Interaction):
    await ctx.response.send_message("test")
    
@commands.command(name="create_new_event")
async def create_new_event(ctx: Interaction, name: str, date: str):
    server_id = ctx.guild_id
    user_id = ctx.user.id
    await input_new_event(server_id=server_id, user_id=user_id, event_name=name, event_date=date)
    await ctx.response.send_message(f"Created Event {name} on {date} by {ctx.user.mention}")

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