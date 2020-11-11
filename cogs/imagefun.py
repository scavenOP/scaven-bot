import discord
from discord.ext import commands
import random
import time
from datetime import datetime
import sys
import os
import traceback
from PIL import Image
from io import BytesIO


class ifun(commands.Cog, name='Moderation'):

    def __init__(self,bot):
        self.bot = bot


    @commands.command()
    async def wanted(self,ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
    
        wanted = Image.open("wanted.jpg")

        asset = user.avatar_url_as(size = 128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((255,255))
        wanted.paste(pfp, (99,201))
        wanted.save("profile.jpg")
        await ctx.send(file = discord.File("profile.jpg"))

    @commands.command()
    async def slap(self,ctx, user: discord.Member):
            
    
        wanted = Image.open("slap.jpg")

        asset = user.avatar_url_as(size = 128)
        asset1 = ctx.author.avatar_url_as(size = 128)
        data = BytesIO(await asset.read())
        data1 = BytesIO(await asset1.read())
        pfp = Image.open(data)
        pfp1 = Image.open(data1)
        pfp = pfp.resize((283,283))
        pfp1 = pfp1.resize((271,271))
        wanted.paste(pfp, (13,443))
        wanted.paste(pfp1, (435,13))
        wanted.save("slapping.jpg")
        await ctx.send(file = discord.File("slapping.jpg"))

    @slap.error
    async def slap_error(self,ctx , error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('would you slap yourself??? mention a member to slap')


    @commands.command()
    async def spank(self,ctx, user: discord.Member):
            
    
        wanted = Image.open("spank.jpg")

        asset = user.avatar_url_as(size = 128)
        asset1 = ctx.author.avatar_url_as(size = 128)
        data = BytesIO(await asset.read())
        data1 = BytesIO(await asset1.read())
        pfp = Image.open(data)
        pfp1 = Image.open(data1)
        pfp = pfp.resize((61,61))
        pfp1 = pfp1.resize((70,70))
        wanted.paste(pfp, (385,148))
        wanted.paste(pfp1, (219,72))
        wanted.save("spanking.jpg")
        await ctx.send(file = discord.File("spanking.jpg"))

    @spank.error
    async def spank_error(self,ctx , error):
            if isinstance(error, commands.MissingRequiredArgument):
                await ctx.send('would you spank yourself??? mention a member to spank')


    @commands.command()
    async def punch(self,ctx, user: discord.Member):
            
    
        punch = Image.open("punch.jpg")

        asset = user.avatar_url_as(size = 128)
        asset1 = ctx.author.avatar_url_as(size = 128)
        data = BytesIO(await asset.read())
        data1 = BytesIO(await asset1.read())
        pfp = Image.open(data)
        pfp1 = Image.open(data1)
        pfp = pfp.resize((74,74))
        pfp1 = pfp1.resize((103,103))
        punch.paste(pfp, (76,209))
        punch.paste(pfp1, (303,99))
        punch.save("punching.jpg")
        await ctx.send(file = discord.File("punching.jpg"))

    @punch.error
    async def punch_error(self,ctx , error):
            if isinstance(error, commands.MissingRequiredArgument):
                await ctx.send('would you punch yourself??? mention a member to spank')


def setup(bot):
    bot.add_cog(ifun((bot)))
    print('cog is loaded!')