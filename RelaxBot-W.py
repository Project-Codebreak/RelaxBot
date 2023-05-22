import discord
import random
from discord.ext import commands

TOKEN = ''

client = commands.Bot(command_prefix = '$')
client.remove_command('help')

@client.event
async def on_ready():
    print("Vibin' ready!")

#Clear command if we want it. Requires some bot permissons
#@client.command()
#async def clear(ctx, amount=5):
    #await ctx.channel.purge(limit=amount + 1)

#Ping command if we want it.
#@client.command()
#async def ping(ctx):
    #await ctx.send(f"Pong! {round (client.latency * 1000)}ms")

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        color = discord.Colour.orange()
    )

    embed.set_author(name='Help')
    embed.add_field(name='.ping', value='Returns Pong', inline=False)
    embed.add_field(name='.hello', value='Says hello back', inline=False)
    embed.add_field(name='.summer', value='Returns a vacation quote', inline=False)

    await author.send(embed=embed)

@client.command()
async def hello(ctx):
    await ctx.send("Hello there!")

@client.command(aliases=['summerQuotes'])
async def summer(ctx):
    responses = ['Friends, sun, sand, and sea, that sounds like summer to me. -Unknown',
                "It's summer and time for wandering... -Kelly Elmore",
                'Smell the sea and feel the sky, let your soul and spirit fly -Salty Soul',
                'Take vacations, go as many places as you can. You can always make money, you cannot always make memories -Unknown',
                'I need a six month vacation twice a year -Unknown',
                'Happiness consists of living each day as if it were the first day of your honeymoon and the last day of your vacation -Leo Tolstoy',
                "A vacation is what you take when you can no longer take what you've been taking -Earl Wilson",
                'Unplug -Unknown',
                'Time for some vitamin sea -Unknown',
                'Time is precious. Waste it wisely -Unknown',
                'A vacation is having nothing to do and having all day to do it -Robert Orben',
                'If you never go, you will never know -Unknown',
                "School's out. Summmer's in. Let the drama stop and the fun begin -Unknown",
                'Time you enjoy wasting was not wasted -Unknown',
                'Live in the sunshine, swim the sea, drink the wild air -Ralph Waldo',
                'B.E.A.C.H Best Escape Anyone Can Have -Unknown']
    await ctx.send(f'{random.choice(responses)}')
    
client.run(TOKEN)
