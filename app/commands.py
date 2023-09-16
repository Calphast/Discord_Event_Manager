import discord
from .database.controller import input_new_event, delete_all_events, display_events, search_for_events, add_user_to_event

from discord import Interaction
from .extentions import commands, clients

@commands.command(name='test')
async def test(ctx: Interaction):
    await ctx.response.send_message("test")
    
@commands.command(name="create_new_event", description="please use year-date-month as date format")
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

@commands.command(name="my_events")
async def get_user_events(ctx: Interaction):
    user_id = ctx.user.id
    events: dict= await display_events(user_id)
    result: str = ""        #instatiated because compiler will freakout if not
    for i in range(len(events)):
        if(i != -1):
            result = result.__add__(str(events[i]))
            result = result.__add__("\n")
    await ctx.response.send_message(f"You have {len(events)} events: \n{result}") 
    
@commands.command(name="find_event")
async def find_event(ctx: Interaction, name_of_event: str):
    server_id = ctx.guild_id
    result: dict = await search_for_events(name_of_event, server_id)
    if (result != []):
        await ctx.response.send_message(result)
    else:
        await ctx.response.send_message("Event not found")
        
@commands.command(name="add_to")
async def add_to_event(ctx: Interaction, event_name: str, user_to_add: discord.User):
    #user_to_add_id: [str]
    #user_to_add_id.append(ctx.message.mentions)
    user_to_add_id = user_to_add.id
    await add_user_to_event(user_id=ctx.user.id, 
                            event_name=event_name, 
                            server_id=ctx.guild_id,
                            user_to_add=str(user_to_add_id))
    await ctx.response.send_message(f"added {user_to_add} to {event_name}")