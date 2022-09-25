import discord
import os
from dotenv import load_dotenv

command_prefix = 'w.'
load_dotenv('.env')
TOKEN = os.getenv('TOKEN')
client = discord.Client(intents=discord.Intents.all())



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'{command_prefix}'))

@client.event
async def on_message(message):
    if message.author != client.user and message.content.startswith(command_prefix):
        await message.channel.send(f'Hi {message.author.mention}')

client.run(TOKEN)