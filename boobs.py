import requests
from random import randint

def get_boobs():
    url = f"http://api.oboobs.ru/boobs/{randint(1, 5000)}/1/rank"
    r = requests.get(url)
    data = r.json()
    preview = data[0].get('preview')
    return f"http://media.oboobs.ru/{preview}"
