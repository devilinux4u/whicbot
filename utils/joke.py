import requests
import json

def get_joke():
    res = requests.get('https://backend-omega-seven.vercel.app/api/getjoke')
    return json.loads(res.text)
