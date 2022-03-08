import requests
import json

def find(word):
    res = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/"+word)
    return json.loads(res.text)