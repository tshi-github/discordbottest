import discord
from discord.ext import commands
from os import getenv

import datetime
today = datetime.date.today()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def start(ctx):
    weekday_message = await checkweekday()
    await ctx.send(weekday_message)

async def checkweekday():
    if today.weekday() == 0:
        return "水曜日の会議室の予約行け！！！"
    elif today.weekday() == 3:
        return "土日月の会議室の予約行け！！！"
    elif today.weekday() == 1 and today.weekday() == 4:
        return "学生課で警備室用の紙を回収せよ！！！"
    else:
        return "日頃の仕事しろ！"

token = getenv('TOKEN')
bot.run('token')
