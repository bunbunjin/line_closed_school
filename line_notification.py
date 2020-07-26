import requests
from okayama_weather import wrn_okayama, adv_okayama
from datetime import time, datetime, date


def line_massage(line_massage_notification):
    token = ''
    line_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {token}'}
    data = {'message': f'message: {line_massage_notification}'}
    requests.post(line_api, headers=headers, data=data)

print(f'\n+++++警報+++++\n')
wrn_okayama()
print(f'\n+++++注意報+++++\n')
adv_okayama()
#line_message('aaa')
