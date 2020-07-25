import requests
from okayama_weather import wrn_okayama
from datetime import time, datetime, date


def line_massage(line_massage_notification):
    token = '4uKZHsEtMh7E3gMZ6H34DO8oovRRWchVXUcKggpzyji'
    line_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {token}'}
    data = {'message': f'message: {line_massage_notification}'}
    requests.post(line_api, headers=headers, data=data)


while True:
    time = datetime.now()
    time_now = str(time)
    now = time_now[10:-7]
    if '07:00:01' == now:
        line_massage(wrn_okayama())
