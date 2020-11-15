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
from disputils import BotEmbedPaginator

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
        channel_id TEXT,
        expchannel_id TEXT)
     ''')

    cursor.close()
    db.close()
    db = sqlite3.connect('leveling.sqlite')
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS levels(
        guild_id TEXT,
        user_id TEXT,
        exp TEXT,
        lvl TEXT,
        rank_exp TEXT)
    ''')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=' ,help | ,info'))
    print("I am Ready!")


@bot.command()
async def help(ctx):
    embed1 = discord.Embed(title="<a:royal:777028611001417768> General Commands <a:royal:777028611001417768>", description="<a:pin1:763647258305757205> **BOT INFO**\n`,info`\n\n<a:pin1:763647258305757205> **INVITE THE BOT**\n`,invite`\n\n<a:pin1:763647258305757205> **SET USER WELCOME**\n`,welcome`\n\n<a:pin1:763647258305757205> **SET EXP Level up Channel**\n`,expchannel`", color=0x0bf9f9, thumbnail= ctx.guild.icon_url)
    embed1.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/773564874822647848/776808076107055154/watermark.png')
    embed2 = discord.Embed(title="<a:royal:777028611001417768> Moderation Commands <a:royal:777028611001417768>", description='<a:pin1:763647258305757205> **CLEAR MESSAGES**\n`,clear <no of messeges>`\n\n<a:pin1:763647258305757205> **EMBED Messages**\n`,say <message>`\n\n<a:pin1:763647258305757205> **KICK MEMBER**\n`,kick <member> <reason>`\n\n<a:pin1:763647258305757205> **BAN MEMBER**\n`,ban <member> <reason>`\n\n<a:pin1:763647258305757205> **UNBAN MEMBER**\n`,unban <member>`\n\n<a:pin1:763647258305757205> **WARN MEMBER**\n`,warn <member> <reason>`', color=0x0bf9f9)
    embed2.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/773564874822647848/776808076107055154/watermark.png')
    embed3 = discord.Embed(title="<a:royal:777028611001417768> Fun Command <a:royal:777028611001417768>", description="<a:pin1:763647258305757205> **SLAP user**\n`,slap <user>`\n\n<a:pin1:763647258305757205> **SPANK user**\n`,spank <user>`\n\n<a:pin1:763647258305757205> **PUNCH user**\n`,punch <user>`\n\n<a:pin1:763647258305757205> **wanted user**\n`,wanted <user>`\n\n<a:pin1:763647258305757205> **SHOW AVATAR**\n`,avatar <member> `", color=0x0bf9f9)
    embed3.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/773564874822647848/776808076107055154/watermark.png')
    embed4 = discord.Embed(title="<a:royal:777028611001417768> SERVER EXP Command <a:royal:777028611001417768>", description="<a:pin1:763647258305757205> **SET Level up Channel**\n`,expchannel <channel>`\n\n<a:pin1:763647258305757205> **Check Level**\n`,level <user>`\n\n<a:pin1:763647258305757205> **Check Server Leaderboard**\n`,explb`", color=0x0bf9f9)
    embed4.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/773564874822647848/776808076107055154/watermark.png')
    
    embeds = [
        embed1,
        embed2,
        embed3,
        embed4
    ]

    paginator = BotEmbedPaginator(ctx, embeds) #This will take all the embeds you provided in the embeds list and will create a paginator.
    await paginator.run()


@bot.command()
async def info(ctx):
    servers = list(bot.guilds)   
    embed = discord.Embed(
    title='<a:royal:777028611001417768> SCAVEN Bot <a:royal:777028611001417768>',
    description=f'\n<a:tools1:763647191414997033> **Made by SCAVEN#2050** <a:tools1:763647191414997033>\n\n\n<a:pin1:763647258305757205> **No of servers bot is present in : {str(len(servers))}**\n\n <a:pin1:763647258305757205> **Invite link :** [Invite me!]({"https://discord.com/api/oauth2/authorize?client_id=766177290542907413&permissions=8&scope=bot"})\n\n<a:pin1:763647258305757205> **Support Server :** [JOIN!]({"https://discord.gg/zhyvbR9UFr"})" ',
    color=0x0bf9f9
    )
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
            'cogs.welcome',
            'cogs.level',
            'cogs.lvlchk']
            
if __name__ == "__main__":
    for extention in extentions:
        try:
            bot.load_extension(extention)
        except Exception as e:
            print(f'Error loading {extention} ', file=sys.stderr)
            traceback.print_exc()






bot.run("NzY2MTc3MjkwNTQyOTA3NDEz.X4fkNA.Z6QCBk0xicFvf142jh22Kv7uo_k")    