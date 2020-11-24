import discord
import random
from api import apiKey
from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.', intents = intents)

@client.event
async def on_ready() :
    print(f'{client.user} is ready')


#MEMBER JOIN AND LEAVE
@client.event
async def on_member_join(member) :
    print(f'{member} has joined a server')

@client.event
async def on_member_remove(member) :
    print(f'{member} has left the server')
#MEMBER JOIN AND LEAVE


@client.command()
async def ping(ctx) :
    pings = [
        'Ki hoyeche bhai kono kaaj nei naki?',
        'Pong!',
        'Ayo whaddup',
        'Humko Disturb mat kario'
    ]
    await ctx.send(random.choice(pings))


@client.command(aliases = ['spam', 'test'])
async def _spam(ctx, user: discord.Member, num) :
    for i in range(int(num)) :
        await ctx.send(f'{user.mention}')


@client.command(aliases = ['future'])
async def _future(ctx, *, member) :
    futures = ['Potty porishkar wala',
               'Harshad Mehta babua',
               'Kyalane',
               'Pro Google coder pola',
               "Xyber's subordinate"]
    await ctx.send(f'{member} will be {random.choice(futures)} in the future')



client.run(apiKey.api_key)
