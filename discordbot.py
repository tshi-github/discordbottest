import discord
from discord.ext import commands
from os import getenv

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

token = getenv('TOKEN')
bot.run(token)
