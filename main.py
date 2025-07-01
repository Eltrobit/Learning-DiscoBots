import discord
import os
import asyncio
from discord.ext import commands

owners = {'675940244490813450', '503171847030964224', '972138097431175208'}
bot = commands.Bot(command_prefix='.', owner_ids=owners, intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("I`m ready!")

#Moderation
banwords = {'хохлы', 'путин', 'putin', 'украина', 'россия', 'росия', 'расия', 'рассия', 'расея', 'рассея'}

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author == bot.user:
        return()

    for i in banwords:
        if i.lower() in message.content.lower():
            print("BANWORD", message.content,  "from", message.author.name, message.author.mention)
            await message.delete()
            break



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

with open("info.txt") as info:
    token = info.read()

bot.run(token)