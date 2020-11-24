import discord
from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.', intents = intents)

@client.event
async def on_ready() :
    print(f'{client.user} is ready')

@client.event
async def on_member_join(member) :
    print(f'{member} has joined a server')

@client.event
async def on_member_remove(member) :
    print(f'{member} has left the server')

client.run('NzgwNjg2MTE2MjQzNjM2MjY1.X7ysmg.R4RqDcP2fPqnUUaojf7xLjLlT8o')
