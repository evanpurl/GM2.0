import os
import sys
import random
import discord
from discord.ext import commands
from discord.ext.commands import has_role

Support = [904120920862519396]

intents = discord.Intents.all()
bot = discord.Bot(intents=intents)

dirr = sys.path[0]  # Main directory path


def tokengrabber():
    if not os.path.exists(f"config/token.txt"):
        with open(f"config/token.txt", "w+") as token:
            tok = input("Input the token for the bot please.")
            token.write(tok)
        return tok
    else:
        with open("config/token.txt", 'r') as token:
            return token.readline()


@bot.event
async def on_ready():
    print("GameMaster 2.0 has been initialized.")
    print(f"We have logged in as {bot.user}")


@bot.event
async def on_guild_join(guild):
    if not os.path.exists(f"{dirr}/servers/{str(guild.id)}"):  # Creates server folder if it does not exist already.
        os.mkdir(f"{dirr}/servers/{str(guild.id)}")
        os.mkdir(f"{dirr}/servers/{str(guild.id)}/Players")


@bot.slash_command(guild_ids=Support, description="Command used to create a unit.")
# @commands.cooldown(rate=1, per=7200, type=commands.BucketType.member)
@has_role("Game Master")
async def createunit(ctx):  # Unit creation command
    pass


@createunit.error
async def create_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        msg = "You don't have the proper role! You require the role 'Game Master'!"
        await ctx.send(msg)
    else:
        print(error)


@bot.slash_command(guild_ids=Support, description="Command used to get the server's units.")
async def units(ctx):
    os.chdir(dirr)
    un = []
    if os.path.exists(f"{os.getcwd()}/Stats/{str(ctx.guild.id)}"):
        filelist = os.listdir(f"{os.getcwd()}/Stats/{str(ctx.guild.id)}")
        if len(filelist) != 0:
            num = 0
            await ctx.respond(f"**{ctx.guild.name}'s Units:**")
            for a, data in enumerate(filelist):
                un.append(f"{a+1}: " + data.replace(".csv", ""))
                if num == 15:
                    await ctx.send('\n'.join(un))
                    num = 0
                    un.clear()
                if a == len(filelist) - 1: # if the last unit has come, and the list isn't empty, send the last units
                    if len(un) != 0:
                        await ctx.send('\n'.join(un))
                num += 1
        else:
            await ctx.respond(
                "No units are currently on the server, create some using the /createunit command!")


@bot.slash_command(guild_ids=Support, description="Command used to create a unit, but quicker.")
# @commands.cooldown(rate=1, per=7200, type=commands.BucketType.member)
@has_role("Design Lead")
async def quickcreate(ctx, name, shields, health, shielddamage, hulldamage, shieldregen):  # Unit creation command
    await ctx.respond(
        f"The unit you tried creating: {name} {shields} {health} {shielddamage} {hulldamage} {shieldregen}")


@quickcreate.error
async def quickcreate_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        msg = "You don't have the proper role! You require admin privileges!"
        await ctx.send(msg)
    else:
        print(error)


bot.run(tokengrabber())
