import datetime
from app.extentions import clients


@clients.command(name='test')
async def test(ctx):
    await ctx.send("test")
    
@clients.command(name="create_new_event")
async def create_new_event(ctx, name: [str], date: datetime):
    pass