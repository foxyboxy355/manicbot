#import statements ================================================================

import discord
from discord.ext import commands
from settings import *
import os
from datetime import datetime
from discord.utils import get

#global vars ======================================================================
initial_extensions = ['cogs.basic']
loaded_extensions = []
bot=commands.Bot(command_prefix='/',description=f'Hi, im ManicBot')
#program functions ================================================================
def time_function():
    now = datetime.now()

    time = now.strftime("[%H:%M:%S]")

    return time

#bot events =======================================================================
@bot.event
async def on_ready():
    print(f"{time_function()}[SUCCESS] Logged in as {bot.user}")
    game = discord.Game("being built...")
    await bot.change_presence(activity=discord.Game(name=game))
    try:
        for extension in initial_extensions:
            bot.load_extension(extension)
            loaded_extensions.append(extension) 

    except:
        print(f"{time_function()}[WARNING] One or more initial extensions not found")

    print(f"{time_function()}[SUCCESS] All extensions loaded")

#bot commands =====================================================================
@bot.command()
async def load(ctx,e):
  if 'cogs.'+e not in initial_extensions:
      print(f"{time_function()}[WARNING] Could not load extension, not an extension")
      await ctx.send(f"The extension you requested ({e}) is not a extension")

  elif ('cogs.'+e) in loaded_extensions:
      print(f"{time_function()}[INFO] Extension already loaded")
      await ctx.send(f"Extension already loaded : {e}")

  else:
    try:
      bot.load_extension('cogs.'+e)
      print(f"{time_function()}[INFO] Loaded extension : {e}")
      loaded_extensions.append('cogs.'+e)
      await ctx.send(f"Loaded extension : {e}")
      channel = bot.get_channel(699965427933249576)
      await channel.send(f'@everyone commands in the category : {e} are now back up and running!') 

    except:
      pass

@bot.command()
async def unload(ctx,e):
  print(f"{time_function()}[INFO] Unloaded extension : {e}")
  bot.unload_extension('cogs.'+e)
  loaded_extensions.remove('cogs.'+e)
  await ctx.send(f"Unloaded extension : {e}")
  channel = bot.get_channel(699965427933249576)
  await channel.send(f'@everyone commands in the category : {e} will be disabled temporarily due to an error in the code') 

@bot.command()
async def reload(ctx,e):
  print(f"{time_function()}[INFO] Reloaded extension : {e}")
  bot.unload_extension('cogs.'+e)
  bot.load_extension('cogs.'+e)
  await ctx.send(f"Reloaded extension : {e}")

@bot.command()
async def show_extensions(ctx):
  print("\nAVAILABLE EXTENSIONS:")
  for i in initial_extensions:
    print(i)

  print("\nLOADED EXTENSIONS")
  for l in loaded_extensions:
    print(l)

  if not loaded_extensions:
      print("NO EXTENSIONS LOADED\n")

@bot.command()
async def clear_terminal(ctx):
  os.system('clear')
  print(f"{bot.user} terminal")
  await ctx.send("Terminal has been cleared")

#run at exec ======================================================================
if __name__ == '__main__':
    os.system('clear')

#run bot ==========================================================================

bot.run(token)