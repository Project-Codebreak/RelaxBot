#This code is to configure relaxBot
import discord

client = discord.Client()

@client.event
async def on_message(message):
    message.content.lower()
    if message.content.startswith("hello"):
        await message.channel.send("Hello, I am a test bot.")

client.run('NzI4NzY5NTQ5NjUwMTAwMjY1.XwCiWQ.VTmc5_t6aPcCAxmeYbXuz71C-Lg')

