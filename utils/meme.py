import requests
import json

def get_meme():
    res = requests.get('https://meme-api.herokuapp.com/gimme')
    data = json.loads(res.text)
    return data['url']