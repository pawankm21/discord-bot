import discord
import random
import requests
from discord.ext import commands
from information import *
from codeforces import contests


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
async def bata(ctx,*,question='nothing'):
    responses= [
        'Trahimum Trahimum bahinchod',
        'Thak gaya hun bro',
        'Nahi   😆',
        'Teri Mummy se puchh'
        '🤡 hat lawde',
    ]
    if(question=='nothing'):
        await ctx.send("Kya bataun?")
    else:
        await ctx.send(random.choice(responses))

@client.command(aliases=['safai','hata'])
async def clear(ctx, amount=5):
    if amount=='all':
        await ctx.send('1000 messages kar raha hun ')
        amount=1000
    await ctx.channel.purge(limit= amount)

@client.command(aliases=['contests','comp'])
async def code(ctx):
    
        await ctx.send(contest)
    
client.run(BOT_KEY) 