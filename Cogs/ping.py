import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        print(f"{ctx.author} asked for ping")
        embed = discord.Embed(title="Ping checkout is here", color=discord.Color.red())
        embed.add_field(name="", value=f"{self.bot.user.name} has latency {round(self.bot.latency * 1000)} ms", inline=False)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Ping(bot))