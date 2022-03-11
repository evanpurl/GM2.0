import discord
from discord.ui import Button, View
from discord.ext import commands
from discord.ext.commands import has_role
import os, sys, random

Support = [904120920862519396]

bot = discord.Bot()
dirr = sys.path[0]  # Main directory path


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.event
async def on_guild_join(guild):
    if not os.path.exists(f"{dirr}/servers/{str(guild.id)}"):  # Creates server folder if it does not exist already.
        os.mkdir(f"{dirr}/servers/{str(guild.id)}")
        os.mkdir(f"{dirr}/servers/{str(guild.id)}/Players")


@bot.slash_command(guild_ids=Support, description="Command used to create a unit.")
# @commands.cooldown(rate=1, per=7200, type=commands.BucketType.member)
@has_role("Design Lead")
async def createunit(ctx):  # Unit creation command
    pass


@createunit.error
async def create_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        msg = "You don't have the proper role! You require admin privileges!"
        await ctx.send(msg)
    else:
        print(error)


@bot.slash_command(guild_ids=Support, description="Command used to create a unit, but quicker.")
# @commands.cooldown(rate=1, per=7200, type=commands.BucketType.member)
@has_role("Design Lead")
async def quickcreate(ctx, name, shields, health, shielddamage, hulldamage, shieldregen):  # Unit creation command
    pass


@quickcreate.error
async def quickcreate_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        msg = "You don't have the proper role! You require admin privileges!"
        await ctx.send(msg)
    else:
        print(error)
