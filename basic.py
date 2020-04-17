
#import statements ================================================================
import discord
from discord.ext import commands
import time
import sys
from datetime import datetime

#global vars ======================================================================
_8ball_answers=['That answer is certain','Without a doubt','Yes- definitley','Possible',"Don't count on it",'Better not tell you know','No','My sources say no','Very unlikely'] 
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

    @commands.command(aliases='8ball')
    async def _8ball(self,ctx,question):
        await ctx.send(f'Your question was: {question}')
        await ctx.send(f'My answer is: {choice(_8ball_answers)}')

#setup cog ========================================================================
def setup(bot):
    bot.add_cog(BasicExtension(bot))