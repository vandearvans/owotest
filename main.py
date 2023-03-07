import discord
import random 
import os
import time
from discord.ext import commands
import colorama
from colorama import Fore
import asyncio
from webserver import keep_alive

print('Please add a secret (env) called "TOKEN", and put your Discord account token in, otherwise it will not work and you will get an error! Confused? Watch YT TUTORIAL: https://www.youtube.com/watch?v=NmC8EDys5Og')
token = (os.environ['TOKEN'])

#-----SETUP-----#

prefix = "-"

#use the .env feature to hide your token

keep_alive()
token = (os.environ['TOKEN'])

#---------------#

bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))
    


print('''THANKS FOR USING THIS SELF BOT IS READY USE -help TO KNOW ALL COMMANDS 

selfbot is ready!
''')


async def owo_levelup(ctx):
    await bot.wait_until_ready()
    channel = bot.get_channel(1082496751962955856)
    while True:
        await channel.send("Owo kiss <@711087102783258697>")
        await asyncio.sleep(60)  # Wait for 1-2 minutes
        await channel.send("owo hug <@1000751730767700070>")
        await asyncio.sleep(60)  # Wait for 1-2 minutes
        await channel.send("Owo Lick <@693831728602677258>")
        await asyncio.sleep(60)  # Wait for 1-2 minutes
        await channel.send("owo cash")
        await asyncio.sleep(60)  # Wait for 1-2 minutes

@bot.command()
async def my_command(ctx):
    bot.loop.create_task(owo_levelup(ctx))




  
keep_alive()
bot.run(token, bot=False)
