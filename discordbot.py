# 土日月は木曜日に絶対取得
# 水曜日は月火曜

import discord
from discord.ext import commands, tasks
import datetime
import os

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    check_time.start()

@tasks.loop(minutes=1)
async def check_time():
    dt_now = datetime.datetime.now()
    if dt_now.hour == 11 and dt_now.minute == 35:
        weekday_message = await checkweekday()
        # CHANNEL_ID を実際のチャンネルIDに置き換えてください
        channel = bot.get_channel('MTI1NDgyMDU1NzYwMjQyNjg5MA.Gcm0B_.HFpUJO07LQUr389ie9gym5J-5JO3oILuiR3SKY')
        if channel:
            await channel.send(weekday_message)

async def checkweekday():
    today = datetime.date.today()
    if today.weekday() == 0:
        return "水曜日の会議室の予約行け！！！"
    elif today.weekday() == 3:
        return "土日月の会議室の予約行け！！！"
    elif today.weekday() in [1, 4]:
        return "学生課で警備室用の紙を回収せよ！！！"

bot.run('MTI1NDgyMDU1NzYwMjQyNjg5MA.Gcm0B_.HFpUJO07LQUr389ie9gym5J-5JO3oILuiR3SKY')
