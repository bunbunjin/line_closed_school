import requests
import time
import schedule
from okayama_alarm import wrn_okayama
from okayama_weather import Weahter


def line_massage(line_massage_notification):
    token = ''
    line_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {token}'}
    data = {'message': f'message: {line_massage_notification}'}
    requests.post(line_api, headers=headers, data=data)


def reserve_mimasaka():
    wrn = wrn_okayama()
    if [] == wrn["美作"]:
        pass
    else:
        line_massage(f'現在、美作市に{wrn["美作"]}警報が発令されています。\n'
                     f'あと10分で決まるぞ！！')
        time.sleep(60)


def decision_mimasaka():
    wrn = wrn_okayama()
    if [] == wrn["美作"]:
        pass
    else:
        line_massage(f'美作市に{wrn["美作"]}警報が発令！！\n学校休み')
        time.sleep(60)


def reserve_okayama():
    wrn = wrn_okayama()
    if [] == wrn["岡山"]:
        pass
    else:
        line_massage(f'現在、岡山市に{wrn["岡山"]}警報が発令されています。\n10分後に期待だ！！！！')


def decision_okayama():
    wrn = wrn_okayama()
    if [] == wrn["岡山"]:
        pass
    else:
        line_massage(f'岡山市に{wrn["岡山"]}警報が出ています')
        time.sleep(60)


def okayama_weather():
    w = Weahter()
    weather = w.okayama_weather()[1]
    print(f'{weather[0]}の天気は{weather[1]}、翌日の{weather[3]}は{weather[4]}です')


schedule.every().day.at('05:50').do(reserve_mimasaka)
schedule.every().day.at('06:00').do(decision_mimasaka)
schedule.every().day.at('06:50').do(reserve_okayama)
schedule.every().day.at('07:00').do(decision_okayama)
schedule.every().day.at('00:00').do(okayama_weather)
while True:
    schedule.run_pending()
