import discord
from discord.ext import commands
import random
import time
from datetime import datetime
import sys
import os
import traceback
import sqlite3

class lvlchk(commands.Cog, name='lvlchk'):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def level(self, ctx, user:discord.User=None):
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

    @commands.command()
    async def explb(self, ctx):
        db = sqlite3.connect('leveling.sqlite')
        cursor = db.cursor()
        cursor.execute(f'SELECT user_id FROM levels  WHERE guild_id = {ctx.message.guild.id} ORDER by rank_exp DESC')
        result = cursor.fetchall()
        res = "\n"
        i = 1
        
        for person in result:
            if i == 10:
                break
            else:
                try:
                    result2 = result = cursor.fetchone()
                    res += f"<a:arrow1:777028732023078932> **{i} : {ctx.guild.get_member(int(person[0]))}**\n\n"
                    i+=1
                except:
                    print(f'Error loading')
        embed=discord.Embed(
            title=(f'<a:star1:763647290014695444> {ctx.message.guild.name} XP Leaderboard <a:star1:763647290014695444>'),
            description=f"\n\n{res}",
            color =0x0bf9f9
        )
        embed.set_thumbnail(url = ctx.guild.icon_url)
        embed.set_footer(text=f'Requested by {ctx.author.name}' , icon_url= ctx.author.avatar_url)
        await ctx.send(embed=embed)
        cursor.close()
        db.close() 




def setup(bot):
    bot.add_cog(lvlchk((bot)))
    print('cog is loaded!')