import os
import discord
from dotenv import load_dotenv

#Time/Date imports
import datetime
import pytz

central = pytz.timezone("US/Central")
japan = pytz.timezone("Japan")

cst = datetime.datetime.now(central)
jst = datetime.datetime.now(japan)

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == "!jst_bot":
        await message.channel.send(cst.strftime("Central Time: %I:%M%p on %A, %B %d %Y"))
        await message.channel.send(jst.strftime("Japan Time: %I:%M%p on %A, %B %d %Y desu")) 

client.run(TOKEN)