import discord
import os
import asyncio
from discord.ext import commands

owners = {'675940244490813450', '503171847030964224', '972138097431175208'}
bot = commands.Bot(command_prefix='.', owner_ids=owners, intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("I`m ready!")


#Turning on

async def Load():
    for filename in os.listdir("./Cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"Cogs.{filename[:-3]}")

with open("info.txt") as info:
    token = info.read()

async def main():
    async with bot:
        await Load()
        await bot.start(token)

asyncio.run(main())