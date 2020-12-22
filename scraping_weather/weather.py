import requests
from bs4 import BeautifulSoup

info = "date", "pict"
links = {}
url = 'https://weather.yahoo.co.jp/weather/jp/33/6610.html'
res = requests.get(url)
html = BeautifulSoup(res.text)
link = html.find(class_="forecastCity").findAll(class_=info)

for count, i in enumerate(link):
    if count % 2 == 0:
        key = link[count].get_text()
    else:
        value = link[count].get_text()
    if count >= 1:
        links[key] = value
print(links)
