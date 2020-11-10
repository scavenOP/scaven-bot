import discord
from discord.ext import commands
import random
import time
from datetime import datetime
import sys
import os
import traceback

class mod(commands.Cog, name='Moderation'):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)   
    async def clear(self,ctx, amount: int):
        await ctx.channel.purge(limit=amount+1)
        embed=discord.Embed(
            description=(f'{amount} messsages deleted !'),
            color = discord.Color.blue()
        )
        await ctx.send(embed=embed, delete_after= 1)
        

    @clear.error
    async def clear_error(self,ctx, error):
        if isinstance(error , commands.MissingRequiredArgument):
            embed=discord.Embed(
            description='Please specify the number of messeges to clear!',
            color = discord.Color.blue()
        )
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self,ctx, member: discord.Member , *, reason=None):
        await member.kick(reason=reason)
        embed=discord.Embed(
            description=(f'{member.name} was successfully kicked for {reason}'),
            color = discord.Color.blue()
        )
        await ctx.send(embed=embed)

    @kick.error
    async def kick_error(self,ctx , error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed1=discord.Embed(
            description='Please mention a user and reason to kick',
            color = discord.Color.blue()
            )
            await ctx.send(embed=embed1)

        elif isinstance(error, commands.MissingPermissions):
            embed=discord.Embed(
            description='You dont have **kick members** permission',
            color = discord.Color.blue()
            )
            await ctx.send(embed=embed)
        raise error
        
        
        

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self,ctx, member: discord.Member , *, reason=None):
        await member.ban(reason=reason)
        embed=discord.Embed(
            description=(f'{member.name} was successfully banned for {reason}'),
            color = discord.Color.blue()
        )
        await ctx.send(embed=embed)

    @ban.error
    async def ban_error(self,ctx , error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed1=discord.Embed(
            description='Please mention a user and a reason to ban',
            color = discord.Color.blue()
            )
            await ctx.send(embed=embed1)

        elif isinstance(error, commands.MissingPermissions):
            embed=discord.Embed(
            description='You dont have Ban members permission',
            color = discord.Color.blue()
            )
            await ctx.send(embed=embed)
        raise error
        

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self,ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if(user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed=discord.Embed(
                description=(f'{user.name} was successfully unbaned'),
                color = discord.Color.blue()
                )
                await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def warn(self,ctx, member: discord.Member , *,args):
        if args != None:
            try:
                await member.send(f'You have been warned : {args}')
                embed=discord.Embed(
                description=(f'{member} was warned for {args}'),
                color = discord.Color.blue()
                )
                await ctx.send(embed=embed)
            except:
                await ctx.send('User has his DMs closed')


    @warn.error
    async def warn_error(self,ctx , error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed1=discord.Embed(
            description='Please mention a user and a reason to warn',
            color = discord.Color.blue()
            )
            await ctx.send(embed=embed1)

        elif isinstance(error, commands.MissingPermissions):
            embed=discord.Embed(
            description='You dont have Manage messages permission',
            color = discord.Color.blue()
            )
            await ctx.send(embed=embed)
        raise error
    
    

        
        


     


def setup(bot):
    bot.add_cog(mod((bot)))
    print('cog is loaded!')