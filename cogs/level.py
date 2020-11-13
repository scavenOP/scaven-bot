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
import  math
import sqlite3


class level(commands.Cog, name='level'):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def expchannel(self, ctx, channel:discord.TextChannel):
            db = sqlite3.connect('welcome.sqlite')
            cursor = db.cursor()
            cursor.execute(f"SELECT expchannel_id FROM welcome WHERE guild_id = {ctx.guild.id}")
            result = cursor.fetchone()
            if result is None:
                sql = ("INSERT INTO welcome(guild_id, expchannel_id) VALUES(?,?)")
                val = (ctx.guild.id, channel.id)
                await ctx.send(f'EXP channel has been set to {channel.mention}')
            elif result is not None:
                sql = ("UPDATE welcome SET expchannel_id = ? WHERE guild_id = ?")
                val = (channel.id, ctx.guild.id)
                await ctx.send(f'EXP channel has been updated to {channel.mention}')
            cursor.execute(sql, val)
            db.commit()
            cursor.close()
            db.close()

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            db = sqlite3.connect('leveling.sqlite')
            cursor = db.cursor()
            cursor.execute(f'SELECT user_id FROM levels WHERE guild_id = {message.guild.id} and user_id = {message.author.id}')
            result = cursor.fetchone()
            if result is None:
                sql = ('INSERT INTO levels(guild_id, user_id, exp, lvl, rank_exp) VALUES(?,?,?,?,?)')
                val = (message.guild.id, message.author.id, 2, 0, 2)
                cursor.execute(sql, val)
                db.commit()
            else:
                cursor.execute(f"SELECT user_id, exp, lvl FROM levels WHERE guild_id = {message.guild.id} and user_id = {message.author.id}")
                result1 = cursor.fetchone()
                
                exp = int(result1[1])
                sql = ('UPDATE levels SET exp = ? WHERE guild_id = ? and user_id = ?')
                val = (exp + 2, str(message.guild.id), str(message.author.id))
                cursor.execute(sql, val)
                sql = ('UPDATE levels SET rank_exp = ? WHERE guild_id = ? and user_id = ?')
                val = (exp + 2, str(message.guild.id), str(message.author.id))
                cursor.execute(sql, val)
                db.commit()
               

                cursor.execute(f'SELECT user_id, exp, lvl FROM levels WHERE guild_id = {message.guild.id} and user_id = {message.author.id}')
                result2 = cursor.fetchone()
                
                xp_start = int(result2[1])
                lvl_start = int(result2[2])
                xp_end = math.floor(5 * (lvl_start ^ 2) + 50 * lvl_start + 100)
                if xp_end < xp_start:
                    db1 = sqlite3.connect('welcome.sqlite')
                    cursor1 = db1.cursor()

                    cursor1.execute(f"SELECT expchannel_id FROM welcome WHERE guild_id = {message.guild.id}")
                    result4 = cursor1.fetchone()
                    channel = message.guild.get_channel(int(result4[0]))
                    if channel != None:
                        await channel.send(f'{message.author.mention} has leveled up to level {lvl_start + 1}.')
                    sql = ('UPDATE levels SET lvl = ? WHERE guild_id = ? and user_id = ?')
                    val = (int(lvl_start + 1), str(message.guild.id), str(message.author.id))
                    cursor.execute(sql, val)
                    db.commit()
                    sql = ('UPDATE levels SET exp = ? WHERE guild_id = ? and user_id = ?')
                    val = (0, str(message.guild.id), str(message.author.id))
                    cursor.execute(sql, val)
                    db.commit()
                    cursor.close()
                    db.close()




    

def setup(bot):
    bot.add_cog(level((bot)))
    print('cog is loaded!')