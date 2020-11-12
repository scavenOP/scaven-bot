import discord
from discord.ext import commands
import random
import time
from datetime import datetime
import sys
import os
import traceback
import sqlite3

class welcome(commands.Cog, name='welcome'):

    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self,member):
        db = sqlite3.connect('welcome.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT channel_id FROM welcome WHERE guild_id = {member.guild.id}")
        result = cursor.fetchone()
        members = len(list(member.guild.members))
        mention = member.mention
        user = member.name
        guild = member.guild
        try:
            cursor.execute(f"SELECT msg FROM welcome WHERE guild_id = {member.guild.id}")
            result1 = cursor.fetchone()
            embed=discord.Embed(
            description=str(result1[0]).format(members=members, mention=mention, user=user, guild=guild),
            color =0x0bf9f9
            )
            channel = self.bot.get_channel(id=int(result[0]))
            await channel.send(embed=embed)
        except Exception as e:
            print(e)


    @commands.group(invoke_without_command=True)
    async def welcome(self,ctx):
        embed=discord.Embed(title='Welcome messege Setup Commands',description='**Set channel to send welcome massege** \n `,welcome channel <#channel>` \n **Set welcome massege** \n `,welcome text <messages>` \n\n **__Available Tags to use in welcome massege__** \n\n',color =0x0bf9f9)
        embed.add_field(name="Name of the user",value='`{user}`', inline = True)
        embed.add_field(name="Mentions the user",value='`{mention}`', inline = True)
        embed.add_field(name="Name of the server",value='`{guild}`', inline = True)
        embed.add_field(name="No of members in the server",value='`{members}`', inline = True)
        await ctx.send(embed=embed)

    @welcome.command()
    @commands.has_permissions(administrator=True)
    async def channel(self, ctx, channel:discord.TextChannel):
            db = sqlite3.connect('welcome.sqlite')
            cursor = db.cursor()
            cursor.execute(f"SELECT channel_id FROM welcome WHERE guild_id = {ctx.guild.id}")
            result = cursor.fetchone()
            if result is None:
                sql = ("INSERT INTO welcome(guild_id, channel_id) VALUES(?,?)")
                val = (ctx.guild.id, channel.id)
                await ctx.send(f'Welcome channel has been set to {channel.mention}')
            elif result is not None:
                sql = ("UPDATE welcome SET channel_id = ? WHERE guild_id = ?")
                val = (channel.id, ctx.guild.id)
                await ctx.send(f'Welcome channel has been updated to {channel.mention}')
            cursor.execute(sql, val)
            db.commit()
            cursor.close()
            db.close()

    @welcome.command()
    @commands.has_permissions(administrator=True)
    async def text(self, ctx, *,text):
            db = sqlite3.connect('welcome.sqlite')
            cursor = db.cursor()
            cursor.execute(f"SELECT msg FROM welcome WHERE guild_id = {ctx.guild.id}")
            result = cursor.fetchone()
            if result is None:
                sql = ("INSERT INTO welcome(guild_id, msg) VALUES(?,?)")
                val = (ctx.guild.id, text)
                await ctx.send(f'Welcome message has been set to {text}')
            elif result is not None:
                sql = ("UPDATE welcome SET msg = ? WHERE guild_id = ?")
                val = (text, ctx.guild.id)
                await ctx.send(f'Welcome message has been updated to `{text}`')
            cursor.execute(sql, val)
            db.commit()
            cursor.close()
            db.close()

    


def setup(bot):
    bot.add_cog(welcome((bot)))
    print('cog is loaded!')