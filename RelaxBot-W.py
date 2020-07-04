import discord

client = discord.Client()

@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("hello"):
        if str(message.author) == "Wessymessy#1893":
            await message.channel.send("No. Go Away.")
        else:
            await message.channel.send("Hello, I am a test bot.")


client.run('NzI4NzY5NTQ5NjUwMTAwMjY1.XwCiWQ.VTmc5_t6aPcCAxmeYbXuz71C-Lg')