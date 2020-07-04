#This code is to configure relaxBot
import discord
import random
from discord.ext import commands

TOKEN = 'NzI4NzY5NTQ5NjUwMTAwMjY1.XwCiWQ.VTmc5_t6aPcCAxmeYbXuz71C-Lg'
client = commands.Bot(command_prefix = '.')


@client.event
async def on_ready():
    print('The bot is ready to start the vibes :)')

@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

