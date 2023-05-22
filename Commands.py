#This code is to configure relaxBot
import discord
from discord.ext import commands
from discord.utils import get
import random
import os

TOKEN = ''
client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print('The bot is ready to start the vibes :)')

@client.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    

    if voice and voice.is_connected:
        await ctx.send(f"Sorry. The bot is currently in use in another voice channel")
    else:
        await channel.connect()
        print('Bot joined the channel.')

@client.command()
async def leave(ctx):
    channel = ctx.message.guild.voice_client
    await channel.disconnect()
    print('Bot lefted the channel.')
client.run(TOKEN)

