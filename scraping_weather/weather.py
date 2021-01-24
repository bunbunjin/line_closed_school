import requests
from bs4 import BeautifulSoup

info = "date", "pict"
url = 'https://weather.yahoo.co.jp/weather/jp/33/6610.html'
links = {}
data = []
res = requests.get(url)
html = BeautifulSoup(res.text)
link = html.find(class_="forecastCity").findAll(class_=info)


def weather():
    for count, i in enumerate(link):
        data.append(link[count].get_text())
        if count % 2 == 0:
            key = link[count].get_text()
        else:
            value = link[count].get_text()
        if count >= 1:
            links[key] = value
    return links, data
