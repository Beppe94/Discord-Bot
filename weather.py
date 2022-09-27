import json
import requests
from dotenv import load_dotenv
import os 

load_dotenv('.env')
API = os.getenv('API') 
command_prefix = 'w.'

def weather(message):
    location = message.content.replace(command_prefix, '')

    if len(location) >= 1:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API}'
        data = requests.get(url).content
        prettyfied = json.loads(data)
        return prettyfied
        
    