import discord
import os
import asyncio
from discord.ext import commands

owners = {'675940244490813450', '503171847030964224', '972138097431175208'}
bot = commands.Bot(command_prefix='.', owner_ids=owners, intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("I`m ready!")
#Commands

@bot.command()
async def pipka(ctx):
    print("pipka from", ctx.message.author.name, ctx.message.author.mention)
    await ctx.send("pipka")

@bot.command(name="Fuck_You")
async def fy(ctx):
    print("FY from", ctx.message.author.name, ctx.message.author.mention)
    await ctx.send("No< Fuck You!")

@bot.command()
async def ping(ctx):
    embed = discord.Embed(title="Ping checkout is here", color=discord.Color.red())
    embed.add_field(name = "", value=f"{bot.user.name} has latency {round(bot.latency * 1000)} ms", inline=False)
    embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url = ctx.author.avatar)
    await ctx.send(embed=embed)



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