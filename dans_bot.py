import discord
import json
from discord.ext.commands import Bot
from discord.ext import commands

with open('.\credentials.json') as creds:
    credentials = json.load(creds)

Client = discord.Client()
bot_prefix = "~"
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
    print ("Bot Online!")
    print ("Name: {}".format(client.user.name))
    print ("ID: {}".format(client.user.id))

@client.command(pass_context=True)
async def ping(ctx):
    await client.say("Pong")

client.run(credentials['client_token'])
