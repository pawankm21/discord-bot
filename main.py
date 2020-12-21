import discord
import random
import requests
from discord.ext import commands
from information import *

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print(ON_READY)

# @client.event
# async def on_message(message):
#      await ctx.send(f'Mass!{round(client.latency*1000)}ms')

@client.event
async def on_member_join(member):
     print(f"Chal {member} jump kar")

@client.event
async def on_member_remove(member):
    print(f"{member} normie ban gaya")
    
@client.command()
async def ping(ctx):
    await ctx.send(f'Pichkari nikli {round(client.latency*1000)}ms mein')

@client.command(aliases =['batao','bhaiyaji'])
async def bata(ctx,*,question):
    responses= [
        'Trahimum Trahimum bahinchod',
        'Thak gaya hun bro',
        'Nahi   😆',
        'Teri Mummy se puchh'
        '🤡 hat lawde',
    ]
    await ctx.send(random.choice(responses))
client.run(BOT_KEY) 