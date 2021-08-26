import os
import discord
from discord.ext import commands
import random
from information import *
from code import future_contests, codeforces_contests
from insults import insults
from jokes import jokes
from youtube import yts
from webserver import keep_alive


client = commands.Bot(command_prefix="[")


@client.event
async def on_ready():
    print(ON_READY)


@client.event
async def on_member_join(member):
    print(f"Chal {member} jump kar")


@client.event
async def on_member_remove(member):
    print(member, REMOVED)


@client.command()
async def ping(ctx):
    await ctx.send(f' ping {round(client.latency*1000)}ms ')


@client.command(aliases=['safai', 'hata', 'delit'])
async def clear(ctx, amount='1'):
    if amount == 'all':
        amount = 1000
    await ctx.send(f'{amount} deleted👌')
    await ctx.channel.purge(limit=int(amount) + 2)


@client.command(aliases=['contests', 'comp', 'cp'])
async def code(ctx, site=None):
    if site is None:
        await ctx.send("please enter codeforces(cp) and codechef(cc)")
    elif site == 'codeforces' or site == 'cf':
        await ctx.send("Here are upcoming contests on CodeForces:")
        for contest in codeforces_contests:
            if contest['phase'] == 'BEFORE':
                await ctx.send(contest['name'])
                await ctx.send(
                    f"https://codeforces.com/contests/{contest['id']}")

    elif site == 'codechef' or 'cc':
        contests = future_contests()
        print(contests)
        await ctx.send(contests)
    else:
        await ctx.send("kripiya sahi site daaliye- codeforces ya codechef")


@client.command(aliases=['batao', 'bhaiyaji', 'tell'])
async def bata(ctx, *, query=None):
    if query == None:
        await ctx.send("Kya bataun")
    else:
        await ctx.send(random.choice(QUESTIONS))


@client.command(aliases=['tareef', 'insult', 'kundli'])
async def compliment(ctx, *, query=None):
    insults_json = insults()
    if query == None:
        message = client.user.name + ', ' + insults_json['insult']
        await ctx.send(message)
    else:
        message = query + ', ' + insults_json['insult']
        await ctx.send(message)


@client.command(aliases=['kamedi', 'majak'])
async def joke(ctx, query="Any"):
    joke_json = jokes(query)
    message = joke_json["joke"]
    await ctx.send(message)


@client.command(aliases=['youtube', 'yt'])
async def YT(ctx, query=None, limit=2):
    if query is None:
        url = yts("trending", limit=2)
        await ctx.send(f"trending on youTube {url}")
    else:
        url = yts(query, limit)
        await ctx.send(url)


@client.command("test")
async def test(ctx, term="this is a test"):
    await ctx.send("this is reply 1")


keep_alive()
BOT_KEY = os.environ.get('BOT_KEY')
client.run(BOT_KEY)
