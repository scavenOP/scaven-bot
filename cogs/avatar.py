import discord
from discord.ext import commands
import random
import time
from datetime import datetime
import sys
import os
import traceback
from discord.utils import get

class avatar(commands.Cog, name='Avatar'):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def avatar(self,ctx, *, user: discord.Member=None):
        if user is None:
            user= ctx.message.author
        
        embed = discord.Embed(
            color = discord.Color.blue()
        )
        embed.add_field(name=user.name,value=f'[Download]({user.avatar_url})')
        embed.set_image(url=user.avatar_url)
        embed.set_footer(text=f'Requested by {ctx.author.name}' , icon_url= ctx.author.avatar_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(avatar((bot)))
    print('cog is loaded!')