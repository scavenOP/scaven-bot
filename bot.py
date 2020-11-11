import discord
from discord.ext import commands
import random
import time
from datetime import datetime
import sys
import os
import traceback
from discord.utils import get

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = ',', intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('type ,cmds for commands'))
    print("I am Ready!")



@bot.command()
async def cmds(ctx):
    embed=discord.Embed(
        description='**CLEAR MESSAGES**\n```,clear <no of messeges>```\n**EMBED Messeges**\n```,say <massege>```\n**KICK MEMBER**\n```,kick <member> <reason>```\n**BAN MEMBER**\n```,ban <member> <reason>```\n**UNBAN MEMBER**\n```,unban <member>```\n**WARN MEMBER**\n```,warn <member> <reason>```\n**SHOW AVATAR**\n```,avatar <member> ```',
        color = discord.Color.blue()
    )
    
    await ctx.send(embed=embed) 

@bot.command()
@commands.has_permissions(manage_messages=True)
async def say(ctx, *,msg):
    embed=discord.Embed(
        description=msg,
        color = discord.Color.blue()
    )
    embed.set_author(name =ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed) 
    await ctx.message.delete()




extentions=['cogs.moderation',
            'cogs.avatar',
            'cogs.imagefun']
            
if __name__ == "__main__":
    for extention in extentions:
        try:
            bot.load_extension(extention)
        except Exception as e:
            print(f'Error loading {extention} ', file=sys.stderr)
            traceback.print_exc()






bot.run("NzY2MTc3MjkwNTQyOTA3NDEz.X4fkNA.Z6QCBk0xicFvf142jh22Kv7uo_k")    