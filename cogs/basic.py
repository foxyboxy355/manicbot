
#import statements ================================================================
import discord
from discord.ext import commands
import time
import sys
from datetime import datetime

#local function ===================================================================
def time_function():
    now = datetime.now()

    time = now.strftime("[%H:%M:%S]")
    return time

#cog class ========================================================================
class BasicExtension(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clear(self,ctx,amount : int):
        print(f"{time_function()}[INFO]{ctx.message.author} cleared {amount} messages from {ctx.channel}")
        await ctx.send(f"Clearing {amount} messages!")
        time.sleep(2)
        await ctx.channel.purge(limit=amount+2)

#setup cog ========================================================================
def setup(bot):
    bot.add_cog(BasicExtension(bot))