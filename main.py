
import os
import discord
from discord.ext import commands
import random
from read import read_json, write_json, append_json
# from code import future_contests, codeforces_contests
from leetcode import Leetcode
from insults import insults
from jokes import jokes
from youtube import yts
from automate import createRoom
from webserver import keep_alive

filename = "information.json"
lc_obj = Leetcode()
client = commands.Bot(command_prefix="[")


@client.event
async def on_ready():
    print("READY")


@client.event
async def on_member_join(member):
    print(f"Chal {member} jump kar")


@client.event
async def on_member_remove(member):
    REMOVED = read_json("REMOVED", filename)
    print(member, REMOVED)


@client.command()
async def ping(ctx):
    """ Check server ping in ms
    """
    await ctx.send(f' ping {round(client.latency*1000)}ms ')


@client.command(aliases=['safai', 'hata', 'delit'])
async def clear(ctx, amount='1'):
    """ Delete messages in bulk
        amount: number of messages to be deleted- default value is 1
        aliases: safai, hata, delit
    """
    if amount == 'all':
        amount = 1000
    await ctx.send(f'{amount} deleted👌')
    await ctx.channel.purge(limit=int(amount) + 2)


# @client.command(aliases=['contests', 'comp', 'cp'])
# async def code(ctx, site=None):
#     """ Search for upcoming contests on codechef and codeforces
#         site: enter the name of site (cf or codeforces,cc or codechef)
#         aliases: contests, comp, cp
#     """
#     if site is None:
#         await ctx.send("please enter codeforces(cp) and codechef(cc)")
#     elif site == 'codeforces' or site == 'cf':
#         await ctx.send("Here are upcoming contests on CodeForces:")
#         for contest in codeforces_contests:
#             if contest['phase'] == 'BEFORE':
#                 await ctx.send(contest['name'])
#                 await ctx.send(
#                     f"https://codeforces.com/contests/{contest['id']}")

#     elif site == 'codechef' or 'cc':
#         contests = future_contests()
#         print(contests)
#         await ctx.send(contests)
#     else:
#         await ctx.send("kripiya sahi site daaliye- codeforces ya codechef")


@client.command(aliases=['lc', 'questions'])
async def leetcode(ctx, query=None, limit=1):
    """ Get a random leetcode question
    queries: name of the question you want to search
    limit: number of questions you want
    aliases: lc, questions
    """
    if query is None:
        await ctx.send(lc_obj.randomQuestion())
    else:
        questions = lc_obj.getByName(query, limit)
        questionstring = ' '.join(questions)
        if questionstring == "":
          await ctx.send("No questions found")
        else:
          await ctx.send(questionstring)

@client.command(aliases=['bs','room'])
async def createroom(ctx):
    """Creates a room at binarysearch.com
    aliases: bs, room
    """
    url=createRoom()
    await ctx.send(url)


@client.command(aliases=['where', 'what'])
async def who(ctx, *, query=None):
    """Random talks
    aliases: where, what
    """
    QUESTIONS = read_json("QUESTIONS", filename)
    if query == None:
        await ctx.send("don't disturb")
    else:
        await ctx.send(random.choice(QUESTIONS))


@client.command(aliases=['tareef', 'compliment', 'kundli'])
async def insult(ctx, *, query=None):
    """  Get a random insult
    aliases: tareef, compliment, kundli
    """
    insults_json = insults()
    if query == None:
        message = client.user.name + ', ' + insults_json['insult']
        await ctx.send(message)
    else:
        message = query + ', ' + insults_json['insult']
        await ctx.send(message)


@client.command(aliases=['kamedi', 'majak'])
async def joke(ctx, query="Any"):
    """ Search for a joke
    aliases: kamedi, majak
    """
    joke_json = jokes(query)
    message = joke_json["joke"]
    await ctx.send(message)


@client.command(aliases=['yt', 'YouTube'])
async def youtube(ctx, query=None, limit=2):
    """Find videos on youtube
    query: the term you want to search, use -underscore instead of spaces
    limit: number of videos
    aliases: yt, YouTube
    """

    if query is None:
        url = yts("trending", limit=2)
        await ctx.send(f"trending on youTube {url}")
    else:
        query.replace('-', ' ')
        url = yts(query, limit)
        urlstring = ' '.join(url)
        await ctx.send(urlstring)


@client.command(aliases=['save', 'put'])
async def setDialogue(ctx, term=None, *args):
  """Saves a dialogue
  aliases: save, put
  """
  if term is not None:
    dialogue = term+' '+' '.join(args)
    append_json("DIALOGUES", dialogue, filename)
    await ctx.send("Successfully added")
  else:
    await ctx.send("Please provide a dialogue")


@client.command(aliases=['say', 'tell'])
async def getDialogue(ctx):
    """ Tells a saved dialogue
    aliases: say, tell
    """
    DIALOGUES = read_json("DIALOGUES", filename)
    index = random.randint(0, len(DIALOGUES)-1)
    await ctx.send(DIALOGUES[index])


@client.command("test")
async def test(ctx, term="this is a test"):
    """This is a test command 
    """
    await ctx.send("this is reply 1")


# keep_alive()
BOT_KEY = os.environ.get('BOT_KEY')
client.run(BOT_KEY)
random.ran
