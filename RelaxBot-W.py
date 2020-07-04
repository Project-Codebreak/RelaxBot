import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("Bot is ready.")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round (client.latency * 1000)}ms")

@client.command(aliases=['summerQuotes'])
async def summer(ctx):
    responses = ['Friends, sun, sand, and sea, that sounds like summer to me.',
                "It's summer and time for wandering...",
                'Smell the sea and feel the sky, let your soul and spirit fly',
                'Take your vacation and let them miss you',
                'I need a six month vacation twice a year',
                'Happiness consists of living each day as if it were the first day of your honeymoon and the last day of your vacatoin',
                "A vacation is what you take when you can no longer take what you've been taking",
                'Unplug',
                'Time for some vitamin sea',
                'Signs point to yes.',
                'Reply hazy, try again.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                'Do not count on it.',
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Very doubtful.']
    await ctx.send(f'{random.choice(responses)}')
    
client.run('NzI4NzY5NTQ5NjUwMTAwMjY1.XwCiWQ.VTmc5_t6aPcCAxmeYbXuz71C-Lg')