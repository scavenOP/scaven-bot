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
    await bot.change_presence(activity=discord.Game('type ,help for commands'))
    print("I am Ready!")


@bot.command()
async def help(ctx):
    embed1 = discord.Embed(title="General Commands", description="**BOT INFO**\n`,info`\n\n**INVITE THE BOT**\n`,invite`\n\n**SET USER WELCOME**\n`,welcome`\n\n**SET EXP Level up Channel**\n`,expchannel`", color=0x0bf9f9, thumbnail= ctx.guild.icon_url)
    embed1.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/773564874822647848/776808076107055154/watermark.png')
    embed2 = discord.Embed(title="Moderation Commands", description='**CLEAR MESSAGES**\n`,clear <no of messeges>`\n\n**EMBED Messeges**\n`,say <massege>\n\n`**KICK MEMBER**\n`,kick <member> <reason>`\n\n**BAN MEMBER**\n`,ban <member> <reason>`\n\n**UNBAN MEMBER**\n`,unban <member>`\n\n**WARN MEMBER**\n`,warn <member> <reason>`\n\n**SEE  EXP  LEVEL**\n`,level `', color=0x0bf9f9)
    embed2.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/773564874822647848/776808076107055154/watermark.png')
    embed3 = discord.Embed(title="Fun Command", description="**SLAP user**\n`,slap <user>`\n\n**SPANK user**\n`,spank <user>`\n\n**PUNCH user**\n`,punch <user>`\n\n**wanted user**\n`,wanted <user>`\n\n**SHOW AVATAR**\n`,avatar <member> `", color=0x0bf9f9)
    embed3.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/773564874822647848/776808076107055154/watermark.png')
    
    embeds = [
        embed1,
        embed2,
        embed3
    ]

    paginator = BotEmbedPaginator(ctx, embeds) #This will take all the embeds you provided in the embeds list and will create a paginator.
    await paginator.run()@bot.command()


@bot.command()
async def info(ctx):
    servers = list(bot.guilds)   
    embed = discord.Embed(
    title='SCAVEN Bot',
    description='**Made by SCAVEN#2050**',
    color=0x0bf9f9
    )
    embed.add_field(name='No of servers bot is present in :',value='**Invite link :**')
    embed.add_field(name=f'{str(len(servers))}',value=f'[Invite me!]({"https://discord.com/api/oauth2/authorize?client_id=766177290542907413&permissions=8&scope=bot"})')   
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


@bot.command()
async def level(ctx, user:discord.User=None):
    if user is None:
        db = sqlite3.connect('leveling.sqlite')
        cursor = db.cursor()
        cursor.execute(f'SELECT user_id, exp, lvl FROM levels WHERE guild_id = {ctx.message.guild.id} and user_id = {ctx.message.author.id}')
        result = cursor.fetchone()
        if result is None:
            embed=discord.Embed(
            title=('**Level Check**'),
            description=(f'**User not ranked**'),
            color =0x0bf9f9
            )
            embed.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=embed) 
            
        else:
            embed1=discord.Embed(
            title=('**Level Check**'),
            description=(f'**{ctx.message.author.name} is currently at level =** `{str(result[2])}` **and has** `{str(result[1])}` **XP**'),
            color =0x0bf9f9
            )
            embed1.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=embed1) 
            cursor.close()
            db.close()
    else:
        db = sqlite3.connect('leveling.sqlite')
        cursor = db.cursor()
        cursor.execute(f'SELECT user_id, exp, lvl FROM levels WHERE guild_id = {ctx.message.guild.id} and user_id = {user.id}')
        result = cursor.fetchone()
        if result is None:
            embed=discord.Embed(
            title=('**Level Check**'),
            description=(f'**User not ranked**'),
            color =0x0bf9f9
            )
            embed.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=embed) 
        else:
            embed1=discord.Embed(
            title=('**Level Check**'),
            description=(f'**{user.name} is currently at level =** `{str(result[2])}` **and has** `{str(result[1])}` **XP**'),
            color =0x0bf9f9
            )
            embed1.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=embed1) 
            cursor.close()
            db.close()





extentions=['cogs.moderation',
            'cogs.avatar',
            'cogs.imagefun',
            'cogs.welcome',
            'cogs.level']
            
if __name__ == "__main__":
    for extention in extentions:
        try:
            bot.load_extension(extention)
        except Exception as e:
            print(f'Error loading {extention} ', file=sys.stderr)
            traceback.print_exc()






bot.run("NzY2MTc3MjkwNTQyOTA3NDEz.X4fkNA.Z6QCBk0xicFvf142jh22Kv7uo_k")    