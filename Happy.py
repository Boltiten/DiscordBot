import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!hello'):
        await message.channel.send('Love you human!')
    
client.run('OTYwNTkzNDIwNzk0MDgxMzAw.YkssVg.cNmDf2bBVqexSfP7aTF2ifpCvWc')
