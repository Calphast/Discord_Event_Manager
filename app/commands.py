from .database.controller import input_new_event, delete_all_events, display_events

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

@commands.command(name="clear_database") 
async def clear_all_events(ctx: Interaction):
    user_id = ctx.user.id
    result = await delete_all_events(user_id=user_id)
    if(result == False):
        await ctx.response.send_message(f"You do not have permission to use this command, you user id = {user_id}")
    elif(result == True):
        await ctx.response.send_message("Database Cleared")


#Unfinished commands:
@commands.command(name="my_events")
async def get_user_events(ctx: Interaction):
    user_id = ctx.user.id
    events: list = await display_events(user_id)
    ctx.message(f"You have {len(events)} active events.")
    for i in len(events):
        ctx.response.send_message(f"{events[i]}")