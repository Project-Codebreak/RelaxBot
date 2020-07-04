#This code is to configure relaxBot
import discord
import random
from discord.ext import commands

TOKEN = 'NzI4NzY5NTQ5NjUwMTAwMjY1.XwCiWQ.VTmc5_t6aPcCAxmeYbXuz71C-Lg'
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('The bot is ready to start the vibes :)')

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
client.run(TOKEN)

