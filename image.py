from http.client import HTTPException
from PIL import Image, ImageSequence
import requests

def resize(message):

    path = '/home/beppe/test/Discord-Bot/Pics'
    res = requests.get(message)
    try:
        open('img.gif', 'wb').write(res.content)
    except HTTPException as e:
        if e == 400:
            print('Error 400')


    return 
