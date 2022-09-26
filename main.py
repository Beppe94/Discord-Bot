import discord
import os
from dotenv import load_dotenv
import PIL

command_prefix = 'w.'
load_dotenv('.env')
TOKEN = os.getenv('TOKEN')
client = discord.Client(intents=discord.Intents.all())



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'{command_prefix}'))


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.author != client.user and message.content.startswith(command_prefix):
        await message.channel.send(f'Hi {message.author.mention}')
    elif 'gif' in message.content:
        await message.channel.send('This is a gif')
        


client.run(TOKEN)