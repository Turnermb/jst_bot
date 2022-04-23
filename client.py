import os
import discord
from dotenv import load_dotenv

#Time/Date imports
import datetime
import pytz

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
client = discord.Client()

central = pytz.timezone("US/Central")
japan = pytz.timezone("Japan")

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == "!japantime" or message.content.lower() == "jst_bot, what time is it in glorious nippon?":
        await message.channel.send(datetime.datetime.now(japan).strftime("It is %I:%M%p on %A, %B %d %Y desu~."))
    elif message.content.lower() == "!kansastime":
        await message.channel.send(datetime.datetime.now(central).strftime("It is %I:%M%p on %A, %B %d %Y."))
client.run(TOKEN)