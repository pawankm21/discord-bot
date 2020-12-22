import discord
import random
import requests
from discord.ext import commands
from information import *
from codeforces import contests_codeforces, contest_id
from datetime import datetime, timedelta
from utils import webc
import bs4 as bs
from time import time
import json

# from smalltalk import SmallTalk


class Contest(object):
    def __init__(self, data):
        self.data = data

    def asdict(self):
        return self.data

    def __eq__(self, other):
        return self.data['description'] == other.data['description']

    def __gt__(self, other):
        return self.data['description'] > other.data['description']

    def __str__(self):
        return self.data['description']

    def __hash__(self):
        return hash(str(self))


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
    print(member, REMOVED)


@client.command()
async def ping(ctx):
    await ctx.send(f'Pichkari nikli {round(client.latency*1000)}ms mein')


@client.command(aliases=['safai', 'hata'])
async def clear(ctx, amount='5'):
    if amount == 'all':
        amount = 1000
    await ctx.send(f'{amount} messages delete kar raha hun ')
    await ctx.channel.purge(limit=int(amount))


#to view codeforces contests
@client.command(aliases=['contests', 'comp'])
async def code(ctx, site='none'):
    if site == 'codeforces':
        await ctx.send("Here are upcoming contests on CodeForces:")
        for name in contests_codeforces:
            await ctx.send(name)
            await ctx.send(f"https://codeforces.com/contest/{contest_id[0]}")
    elif site == 'codechef':
        contests = await webc.webget_text('https://www.codechef.com/contests/')
        soup = bs.BeautifulSoup(contests, 'lxml')
        for contest in soup.find_all('table',
                                     attrs={'class': 'dataTable'
                                            })[1].find('tbody').find_all('tr'):
            details = contest.find_all('td')
            if datetime.strptime(
                    details[2].attrs['data-starttime'].split('+')[0] + '+' +
                    details[2].attrs['data-starttime'].split('+')[1].replace(
                        ':', ''), '%Y-%m-%dT%H:%M:%S%z').timestamp() >= time():
                contest_data = {
                    'title':
                    ':trophy: %s' % details[1].find('a').contents[0],
                    'description':
                    'https://www.codechef.com/' + details[0].contents[0],
                    'oj':
                    'codechef',
                    'Start Time':
                    (details[2].attrs['data-starttime'].split('+')[0] + '+' +
                     details[2].attrs['data-starttime'].split('+')[1].replace(
                         ':', '')).replace('T', ' '),
                    'End Time':
                    (details[3].attrs['data-endtime'].split('+')[0] + '+' +
                     details[3].attrs['data-endtime'].split('+')[1].replace(
                         ':', '')).replace('T', ' ')
                }
                codechef_contest_titles = []
                codechef_contests = []
                if contest_data['title'] not in codechef_contest_titles:
                    codechef_contest_titles.append(contest_data['title'])
                    codechef_contests.append(Contest(contest_data))
        codechef_contests = list(set(codechef_contests))

        await ctx.send(contest_data['title'])
        await ctx.send(contest_data['description'])
        await ctx.send(f"From: {contest_data['Start Time']}")
        await ctx.send(f" To: {contest_data['End Time']}")

    else:
        await ctx.send("sahi site daal- codeforces nahi to codechef")


@client.command(aliases=[
    'batao',
    'bhaiyaji',
])
async def bata(ctx, *, query=None):
    if query == None:
        await ctx.send("Kya bataun")
    else:
        await ctx.send(random.choice(RESPONSES))


# @client.command(aliases=['angrezi','!'])
# async def talk(ctx,*,query='helo'):
#     if smalltalk.intent =='''"sentiment.curse"''':
#         await ctx.send("MAA BAAP NE YAHI SIKHAYA HAI 😡")
#     else :
#         await ctx.send(smalltalk.talkback)
#     print(smalltalk.response.text)


@client.command(aliases=['tareef', 'insult', 'kundli'])
async def compliment(ctx, *, query=None):
    url = "https://evilinsult.com/generate_insult.php?lang=en&type=json"
    r = requests.get(url)
    insults_json = r.json()
    print()

    if query == None:
        message = client.user.name + ', ' + insults_json['insult']
        await ctx.send(message)
    else:
        message = query + ', ' + insults_json['insult']
        await ctx.send(message)


client.run(BOT_KEY)
