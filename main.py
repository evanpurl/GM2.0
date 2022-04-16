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

gm = bot.create_group('gm', 'Gamemaster command prefix')


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
    print(f"Py-Cord version: {discord.__version__}")
    await bot.change_presence(activity=discord.Game('Powered by NLS: https://www.nitelifesoftware.com'))


@bot.event
async def on_guild_join(guild):
    if not os.path.exists(f"{dirr}/servers/{str(guild.id)}"):  # Creates server folder if it does not exist already.
        os.mkdir(f"{dirr}/servers/{str(guild.id)}")
        os.mkdir(f"{dirr}/servers/{str(guild.id)}/Players")


@gm.command(guild_ids=Support, description="Command used to create a unit.")
# @commands.cooldown(rate=1, per=7200, type=commands.BucketType.member)
async def createunit(ctx):  # Unit creation command
    role = discord.utils.get(ctx.guild.roles, name="Game Master")
    if role in ctx.user.roles:
        await ctx.respond("WIP")
    else:
        await ctx.respond("You do not have the proper role to run this command. Required role: **Game Master**")


@gm.command(guild_ids=Support, description="Command used to get the server's units.")
async def units(ctx):
    os.chdir(dirr)
    un = []
    if os.path.exists(f"{os.getcwd()}/Stats/{str(ctx.guild.id)}"):
        filelist = os.listdir(f"{os.getcwd()}/Stats/{str(ctx.guild.id)}")
        if len(filelist) != 0:
            num = 0
            await ctx.respond(f"**{ctx.guild.name}'s Units:**")
            for a, data in enumerate(filelist):
                un.append(f"{a + 1}: " + data.replace(".csv", ""))
                if num == 15:
                    await ctx.send('\n'.join(un))
                    num = 0
                    un.clear()
                if a == len(filelist) - 1:  # if the last unit has come, and the list isn't empty, send the last units
                    if len(un) != 0:
                        await ctx.send('\n'.join(un))
                num += 1
        else:
            await ctx.respond(
                "No units are currently on the server, create some using the /createunit command!")


@gm.command(guild_ids=Support, description="Command used to create a unit, but quicker.")
# @commands.cooldown(rate=1, per=7200, type=commands.BucketType.member)
async def quickcreate(ctx, name, shields, health, sdamage, damage, shieldregen):  # Unit creation command
    role = discord.utils.get(ctx.guild.roles, name="Game Master")
    if role in ctx.user.roles:
        with open(f"{dirr}/Stats/{str(ctx.guild.id)}/{name}.csv", "w+") as csv_file:
            csv_file.write(
                f"{name}\nHealth: {health}\nShield: {shields}\nShield Regen: {shieldregen}\nShield Damage: {sdamage}\nDamage: {damage}")
        await ctx.respond(f"Unit with the name {name} has been created.")
    else:
        await ctx.respond("You do not have the proper role to create units. Required role: Game Master")


bot.run(tokengrabber())
