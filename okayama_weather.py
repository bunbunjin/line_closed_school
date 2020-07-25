import requests
from bs4 import BeautifulSoup


warn = "wrn", "il1"
adv_ = "adv", "il2"
city = {
    0: "岡山",
    1: "玉野",
    2: "瀬戸内",
    3: "吉備中央",
    4: "備前",
    5: "赤磐",
    6: "和気",
    7: "倉敷",
    8: "総社",
    9: "早島",
    10: "笠岡",
    11: "井原",
    12: "浅口",
    13: "里庄",
    14: "矢掛",
    15: "高梁",
    16: "新見",
    17: "真庭",
    18: "新庄",
    19: "津山",
    20: "鏡野",
    21: "久米南",
    22: "美咲",
    23: "美作",
    24: "勝央",
    25: "奈義",
    26: "西栗倉",
}
adv = {
    0: "大雨",
    1: "洪水",
    2: "強風",
    3: "風雪",
    4: "大雪",
    5: "波浪",
    6: "高潮",
    7: "雷",
    8: "融雪",
    9: "濃霧",
    10: "乾燥",
    12: "なだれ",
    13: "低温",
    14: "霜",
    15: "着氷",
    16: "着雪",
}
wrn = {
    0: "大雨",
    1: "洪水",
    2: "暴風 ",
    3: "暴風雪",
    4: "大雪",
    5: "波浪",
    6: "高潮",

}
wrn_chars_str = []
adv_chars_str = []

res = requests.get('https://www.jma.go.jp/jp/warn/340_table.html')
html = BeautifulSoup(res.text)
links = html.findAll(class_=warn)
link = html.findAll(class_=adv_)

for char in links:
    chars = str(char)
    wrn_chars_str.append(chars)

for char in link:
    chars = str(char)
    adv_chars_str.append(chars)

place_warn = [wrn_chars_str[i:i+7] for i in range(0, len(wrn_chars_str), 7)]
place_adv = [adv_chars_str[i:i+16] for i in range(0, len(adv_chars_str), 16)]

for count, i in enumerate(place_warn):
    print(f'{city[count]}::{place_warn[count]}')
print('\n-----------------------------------------------------------------\n')

for count, i in enumerate(place_adv):
    print(f'{city[count]}::{place_adv[count]}')


def wrn_okayama():
    for count, i in enumerate(place_warn):
        print(f'====={city[count]}======')
        for con, e in enumerate(i):
            if '<td class="wrn"></td>' == e:
                pass
            elif '<td class="il1"></td>' == e:
                pass
            else:
                print(f'{wrn[con]}')
                if count == 0:
                    return wrn[con]


def adv_okayama():
    for count_, i in enumerate(place_adv):
        print(f'====={city[count_]}=====')
        for con, e in enumerate(i):
            if '<td class="adv"></td>'  == e:
                pass
            elif '<td class="il2"></td>' == e:
                pass
            else:
                print(f'{adv[con]}')
                continue


wrn_okayama()
print('--------------------')
adv_okayama()
