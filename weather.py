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
        data_list = []
        data_list.append(prettyfied['weather'])
        data_list.append(temp_c(prettyfied['main']))
        return data_list
        
    
def temp_c(data_dict):
    for k,v in data_dict.items():
        if k == 'temp' or k == 'feels_like' or k == 'temp_min' or k == 'temp_max':
            data_dict[k] = v - 273.15
        else:
            data_dict[k] = v
    return data_dict