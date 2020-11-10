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


@bot.event
async def on_member_join(member):
    try:
        channel = bot.get_channel(775257002199875604)
        embed=discord.Embed(
        description=(f'**<a:woo:763647295027544085> HeY {member.mention}   <a:wel:763647213825556492><a:com:763647211362844692>  To SCAVEN PLAYS <a:woo:763647295027544085> \n<a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610>\n<a:pan:763647268502896700> BE SURE TO CHECK  <a:pan:763647268502896700> \n<a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610>\n<a:pin:763647258305757205> │READ** <#763740922847428609>   **AND FOLLOW\n<a:pin:763647258305757205> │ GRAB** <#763653900087590912>  **AND DEFINE YOURSELF \n<a:pin:763647258305757205> │NOW GO TO** <#763748860609822760>  **AND HAVE FUN \n<a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610><a:e_:763755807971737610>\n<a:blueheart:763647193893699605> <a:skyheart:763647194115997697> <a:neons:763647324731473952> <a:neonc:763647327566168076> <a:neona:763647323086913536> <a:neonv:763647318175383565> <a:neone:763647333010374666> <a:neonn:763647334520324097> <a:skyheart:763647194115997697> <a:blueheart:763647193893699605>**'),
        color = discord.Color.blue()
        )
        await channel.send(embed=embed)
    except Exception as e:
        print(e)

@bot.event
async def on_member_remove(member):
    try:
        channel = bot.get_channel(775257002199875604)
        embed=discord.Embed(
        description=f' {member.name} just left the server <:kid2:763761247853477928> ',
        color = discord.Color.blue()
        )
        await channel.send(embed=embed)
    except Exception as e:
        print(e)

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