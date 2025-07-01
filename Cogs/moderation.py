import discord
from discord.ext import commands

banwords = {'хохлы', 'путин', 'putin', 'украина', 'россия', 'росия', 'расия', 'рассия', 'расея', 'рассея'}

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        await self.bot.process_commands(message)
        if message.author == self.bot.user:
            return

        for i in banwords:
            if i.lower() in message.content.lower():
                print("BANWORD", message.content, "from", message.author.name, message.author.mention)
                await message.delete()
                break

async def setup(bot):
    await bot.add_cog(Moderation(bot))