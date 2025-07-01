import discord
from discord.ext import commands

owners = {'675940244490813450', '503171847030964224', '972138097431175208'}
banwords = {'хохлы', 'путин', 'putin'}
bot = commands.Bot(command_prefix='.', owner_ids=owners, intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("I`m ready!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return()

    for i in banwords:
        if i.lower() in message.content.lower():
            print("BANWORD", message.content,  "from", message.author.name, message.author.mention)
            await message.delete()
            break

with open("info.txt") as info:
    token = info.read()

bot.run(token)