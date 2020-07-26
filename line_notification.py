import requests
import time
from okayama_weather import wrn_okayama
from datetime import datetime


def line_massage(line_massage_notification):
    token = ''
    line_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {token}'}
    data = {'message': f'message: {line_massage_notification}'}
    requests.post(line_api, headers=headers, data=data)


while True:
    tim = str(datetime.now())
    now = tim[11:]

    if '06:50' == now:
        wrn = wrn_okayama()
        if [] == wrn["岡山"]:
            pass
        else:
            line_massage(f'現在、岡山市に{wrn["岡山"]}警報が発令されています。\n10分後に期待だ！！！！')
            time.sleep(60)

    if '07:00' == now:
        wrn = wrn_okayama()
        if [] == wrn["岡山"]:
            pass
        else:
            line_massage(f'岡山市に{wrn["岡山"]}警報が出ています')
            time.sleep(60)
