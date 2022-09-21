from genericpath import exists
from operator import countOf
from discord.ext import commands
import discord
from discord import Permissions
import random
from discord.utils import get
from discord import Embed
from aiohttp import ClientSession


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.presences = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 905926465781133313  # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.listen('on_message')
async def on_message(message):
    if message.content == "Salut tout le monde":
        await message.channel.send(f"Salut tout seul {message.author.mention}")
        return

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.command()
async def name(ctx):
    await ctx.send(ctx.author.name)

@bot.command()
async def d6(ctx):
    list1 = [1, 2, 3, 4, 5, 6]
    await ctx.send(random.choice(list1))

@bot.command()
async def admin(ctx,arg1):
    if not get(ctx.guild.roles, name="Admin"):
        await ctx.guild.create_role(name='Admin', permissions=discord.Permissions(8))

    user = get(bot.get_all_members(), nick=arg1)
    if user:
        role = get(ctx.message.guild.roles, name ="Admin")
        await user.add_roles(role)
    else:
        user = get(bot.get_all_members(), name=arg1)
        if user:
            role = get(ctx.message.guild.roles, name ="Admin")
            await user.add_roles(role)


@bot.command()
async def ban(ctx,arg1):
    user = get(bot.get_all_members(), nick=arg1)
    if user:
        await ctx.guild.ban(user)
    else:
        user = get(bot.get_all_members(), name=arg1)
        if user:
            await ctx.guild.ban(user)

@bot.command()
async def count(ctx):
    countOnline = 0
    countIdle = 0
    countOffline = 0
    countDnd = 0

    for member in ctx.guild.members:
        if(member.status == discord.Status.online):
            countOnline +=1
        elif(member.status == discord.Status.offline):
            countOffline +=1
        elif(member.status == discord.Status.idle):
            countIdle +=1
        elif(member.status == discord.Status.dnd):
            countDnd +=1
    await ctx.send(str(countOnline) + " member online, " + str(countIdle) + " are idle " + str(countDnd) + " are in do not disturb and " + str(countOffline) + " are off")

@bot.command()
async def poll(ctx, question):
    await ctx.send(question + " @here")
    message = await ctx.send(question)
    await message.add_reaction('\N{THUMBS UP SIGN}')
    await message.add_reaction('\N{THUMBS DOWN SIGN}')

token = ""
bot.run(token)  # Starts the bot