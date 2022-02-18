import discord 
from discord.ext import commands

class Echo(commands.Cog):
    #initiate the class 
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def echo(ctx, *, arg):
        await ctx.send(arg)

def setup(client):
    client.add_cog(Echo(client))
