import discord
from discord.ext import commands
import random
import time
from datetime import datetime
import sys
import os
import traceback
from discord.utils import get
import sqlite3

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = ',', intents=intents)
bot.remove_command('help')

@bot.event
async def on_ready():
    db = sqlite3.connect('welcome.sqlite')
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS welcome(
        guild_id TEXT,
        msg TEXT,
        channel_id TEXT)
     ''')
    await bot.change_presence(activity=discord.Game('type ,help for commands'))
    print("I am Ready!")


@bot.command()
async def help(ctx):
    embed=discord.Embed(
        description='**Moderater commands **\n```,modcmd ```\n**SET Welcome message **\n```,welcome ```\n**Fun commands**\n```,fun ```\n**INVITE ME**\n```,invite ```\n**Bot info**\n```,info```',
        color =0x0bf9f9
    )
    
    await ctx.send(embed=embed) 

@bot.command()
async def info(ctx):
        
    embed = discord.Embed(
    title='SCAVEN Bot',
    description='**Made by SCAVEN#2050**',
    color=0x0bf9f9
    )
    embed.add_field(name='👇👇Invite Link!',value=f'[Invite me!]({"https://discord.com/api/oauth2/authorize?client_id=766177290542907413&permissions=8&scope=bot"})')   
    embed.set_image(url="https://cdn.discordapp.com/attachments/773564874822647848/776362486298705930/watermark.png")
    embed.set_footer(text=f'Requested by {ctx.author.name}' , icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)


@bot.command()
async def invite(ctx):
    embed=discord.Embed(
        title='Invite the bot to your server',
        color =0x0bf9f9
    )
    embed.add_field(name='Click on `Invite me!`',value=f'[Invite me!]({"https://discord.com/api/oauth2/authorize?client_id=766177290542907413&permissions=8&scope=bot"})')
    await ctx.send(embed=embed) 


@bot.command()
async def modcmd(ctx):
    embed=discord.Embed(
        description='**CLEAR MESSAGES**\n```,clear <no of messeges>```\n**EMBED Messeges**\n```,say <massege>```\n**KICK MEMBER**\n```,kick <member> <reason>```\n**BAN MEMBER**\n```,ban <member> <reason>```\n**UNBAN MEMBER**\n```,unban <member>```\n**WARN MEMBER**\n```,warn <member> <reason>```',
        color =0x0bf9f9
    )
    
    await ctx.send(embed=embed) 


@bot.command()
async def fun(ctx):
    embed=discord.Embed(
        description='**SLAP user**\n```,slap <user>``` \n**SPANK user**\n```,spank <user>```\n**PUNCH user**\n```,punch <user>```\n**wanted user**\n```,wanted <user>```\n**SHOW AVATAR**\n```,avatar <member> ```',
        color =0x0bf9f9
    )
    
    await ctx.send(embed=embed) 

@bot.command()
@commands.has_permissions(manage_messages=True)
async def say(ctx, *,msg):
    embed=discord.Embed(
        description=msg,
        color =0x0bf9f9
    )
    embed.set_author(name =ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed) 
    await ctx.message.delete()




extentions=['cogs.moderation',
            'cogs.avatar',
            'cogs.imagefun',
            'cogs.welcome']
            
if __name__ == "__main__":
    for extention in extentions:
        try:
            bot.load_extension(extention)
        except Exception as e:
            print(f'Error loading {extention} ', file=sys.stderr)
            traceback.print_exc()






bot.run("NzY2MTc3MjkwNTQyOTA3NDEz.X4fkNA.Z6QCBk0xicFvf142jh22Kv7uo_k")    