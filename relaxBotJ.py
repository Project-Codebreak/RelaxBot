#This code is to configure relaxBot
import os
import discord

client = discord.Client()

@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("hello"):
        await message.channel.send("Hello, I am a test bot.")
    if message.author == "Wessymessy#1893":
        await message.channel.send("No. Go Away.")
    if message.author == "Raging_Beast#4944":
        await message.channel.send("Hi! You're Awesome!")


client.run('NzI4NzY5NTQ5NjUwMTAwMjY1.XwCiWQ.VTmc5_t6aPcCAxmeYbXuz71C-Lg')