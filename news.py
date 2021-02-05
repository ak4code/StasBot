import requests
from xml.etree import ElementTree
from random import randint

news = []

def update_feed():
    r = requests.get('https://lenta.ru/rss')
    root = ElementTree.fromstring(r.content)
    for item in root.iter('item'):
        news.append({'title': item.find('title').text, 'link': item.find('link').text, 'description': item.find('description').text})

def get_news():
    news.clear()
    update_feed()
    item = news[randint(1, 10)]
    return f"<b>{item.get('title')}</b>{item.get('description')}{item.get('link')}"

