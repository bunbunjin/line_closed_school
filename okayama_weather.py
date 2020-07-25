import requests
from bs4 import BeautifulSoup

word = "adv", "il2"

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
chars_str = []

res = requests.get('https://www.jma.go.jp/jp/warn/340_table.html')
html = BeautifulSoup(res.text)
links = html.findAll(class_=word)
print(links)

for char in links:
    chars = str(char)
    chars_str.append(chars)

a = [chars_str[i:i+16] for i in range(0, len(chars_str), 16)]
print(a)
for aa, ww in enumerate(a):
    print(f'{city[aa]}{a[aa]}')
print('\n-----------------------------------------------------------------\n')
for count, i in enumerate(a):
    print(f'====={city[count]}======')
    for con, e in enumerate(i):
        if e == '<td class="adv">●</td>':
            print(f'{adv[con]}')
