#This code is to configure relaxBot
import discord
from discord.ext import commands
from discord.utils import get
import random
import os


TOKEN = 'NzI4NzY5NTQ5NjUwMTAwMjY1.XwCiWQ.VTmc5_t6aPcCAxmeYbXuz71C-Lg'
client = commands.Bot(command_prefix = '.')


@client.event
async def on_ready():
    print('The bot is ready to start the vibes :)')

@client.command()
async def join(ctx):
    async def join(ctx):
        channel = ctx.message.author.voice.channel
        await client.join_voice_channel(channel)

    print('Bot joined the channel.')


client.run(TOKEN)

