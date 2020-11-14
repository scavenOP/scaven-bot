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
        cursor.execute(f'SELECT user_id, rank_exp FROM levels  WHERE guild_id = {ctx.message.guild.id} ORDER by rank_exp DESC')
        result = cursor.fetchall()
        try:
            rank1 = (ctx.guild.get_member(int(result[0][0]))).name
            exp1= int(result[0][1])
        except:
            rank1 = 'None'
            exp1 = '0'
        try:
            rank2= (ctx.guild.get_member(int(result[1][0]))).name
            exp2= int(result[1][1])
        except:
            rank2 = 'None'
            exp2 = '0'
        try:
            rank3= (ctx.guild.get_member(int(result[2][0]))).name
            exp3= int(result[2][1])
        except:
            rank3 = 'None'
            exp3 = '0'
        try:
            rank4= (ctx.guild.get_member(int(result[3][0]))).name
            exp4= int(result[3][1])
        except:
            rank4 = 'None'
            exp4 = '0'
        try:
            rank5= (ctx.guild.get_member(int(result[4][0]))).name
            exp5= int(result[4][1])
        except:
            rank5 = 'None'
            exp5 = '0'
        try:
            rank6= (ctx.guild.get_member(int(result[5][0]))).name
            exp6= int(result[5][1])
        except:
            rank6 = 'None'
            exp6 = '0'
        try:
            rank7= (ctx.guild.get_member(int(result[6][0]))).name
            exp7= int(result[6][1])
        except:
            rank7 = 'None'
            exp7 = '0'
        try:
            rank8= (ctx.guild.get_member(int(result[7][0]))).name
            exp8= int(result[7][1])
        except:
            rank8 = 'None'
            exp8 = '0'
        try:
            rank9= (ctx.guild.get_member(int(result[8][0]))).name
            exp9= int(result[8][1])
        except:
            rank9 = 'None'
            exp9 = '0'
        try:
            rank10= (ctx.guild.get_member(int(result[9][0]))).name
            exp10= int(result[9][1])
        except:
            rank10 = 'None'
            exp10 = '0'
        
        embed=discord.Embed(
            title=(str(f'<a:star1:763647290014695444> {ctx.message.guild.name} XP Leaderboard <a:star1:763647290014695444>',)),
            description=(f"**\n\n <a:arrow1:777028732023078932> 1. {rank1} with total XP {exp1}\n\n<a:arrow1:777028732023078932> 2. {rank2} with total XP {exp2}\n\n<a:arrow1:777028732023078932> 3. {rank3} with total XP {exp3}\n\n<a:arrow1:777028732023078932> 4. {rank4} with total XP {exp4}\n\n<a:arrow1:777028732023078932> 5. {rank5} with total XP {exp5}\n\n<a:arrow1:777028732023078932> 6. {rank6} with total XP {exp6}\n\n<a:arrow1:777028732023078932> 7. {rank7} with total XP {exp7}\n\n<a:arrow1:777028732023078932> 8. {rank8} with total XP {exp8}\n\n<a:arrow1:777028732023078932> 9. {rank9} with total XP {exp9}\n\n<a:arrow1:777028732023078932> 10. {rank10} with total XP {exp10}**"),
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