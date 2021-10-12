
from os import environ
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
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.all()
discord.member = True
filename = "information.json"
lc_obj = Leetcode()
client = commands.Bot(command_prefix="[")


@client.event
async def on_ready():
    print("READY")


@client.event
async def on_ready():
    """
    prints READY on ready
    """
    print("READY")


@client.event
async def on_member_join(member):
    channel = client.get_channel(int(environ.get("WELCOME")))
    await channel.send(f"{member} Welcome my friend😀")


@client.event
async def on_message(message):
    """
    Event triggered on message
    """
    QUESTIONS = read_json("QUESTIONS", filename)
    if(message.author == client.user):
        return
    if client.user in message.mentions:
        await client.get_channel(message.channel.id).send(random.choice(QUESTIONS)+"🤖")
    await client.process_commands(message)


@client.event
async def on_member_remove(member):
    """
    Event triggered when member is removed
    """
    channel = client.get_channel(int(environ.get("WELCOME")))
    await channel.send(f"{member} left the server.😔")



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


@client.command()
async def joke(ctx, query="Any"):
    """ Search for a joke
    query: Programming/Misc/Dark/Pun/Spooky/Christmas
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


@commands.has_permissions(kick_members=True)
@client.command()
async def kick(ctx, user: discord.Member, *, reason=None):
    """
        kicks user
        user: Mention user
    """
    await user.kick(reason=reason)
    await ctx.send(f'User {user} has kicked.')


@commands.has_permissions(ban_members=True)
@client.command()
async def ban(ctx, user: discord.Member, *, reason="bad behaviour"):
    """
    bans user
    user: Mention user
    """
    await user.ban(reason=reason)
    ban = discord.Embed(
        title=f":boom: Banned {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    await ctx.message.delete()
    await ctx.channel.send(embed=ban)
    await user.send(embed=ban)


@client.command()
async def unban(ctx, *, member):
    """
    unbans user
    user: Mention user
    """
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')



BOT_KEY = environ.get('BOT_KEY')
client.run(BOT_KEY)

