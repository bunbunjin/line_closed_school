import requests
from bs4 import BeautifulSoup


#ToDo:気象庁のHPの再スクレイピング（HP）

wrn_ = "wrn", "il1"
adv_ = "warning-summary-sentence", "warning-summary-box contents-level20"

city = {
    0: " 岡山市",
    1: " 玉野市",
    2: " 瀬戸内市",
    3: " 吉備中央町",
    4: " 備前市",
    5: " 赤磐市",
    6: " 和気市",
    7: " 倉敷市",
    8: " 総社市",
    9: " 早島市",
    10: " 笠岡市",
    11: " 井原市",
    12: " 浅口市",
    13: " 里庄市",
    14: " 矢掛市",
    15: " 高梁市",
    16: " 新見市",
    17: " 真庭市",
    18: " 新庄市",
    19: " 津山市",
    20: " 鏡野町",
    21: " 久米南町",
    22: " 美咲町",
    23: " 美作市",
    24: " 勝央町",
    25: " 奈義町",
    26: " 西栗倉町",
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
    11: "なだれ",
    12: "低温",
    13: "霜",
    14: "着氷",
    15: "着雪",
}
wrn = {
    0: "大雨",
    1: "洪水",
    2: "強風",
    3: "暴風雪",
    4: "大雪",
    5: "波浪",
    6: "高潮",
}
wrn_chars_str = []
adv_chars_str = []

res = requests.get('https://typhoon.yahoo.co.jp/weather/jp/warn/33/')
html = BeautifulSoup(res.text, "html.parser")

okayama_ = html.find(class_="warnArea_box").find("table").get_text(", ", strip=True)
delete_word = ['南部', ' 岡山地域', ' 倉敷地域', ' 井笠地域', ' 高梁地域', ' 東備地域', ' 津山地域', ' 新見地域', ' 真庭地域', ' 勝英地域', ' 北部']
city_list = [" 岡山市", " 玉野市", " 瀬戸内市", " 吉備中央町", " 備前市", " 赤磐市", " 和気市", " 倉敷市", " 総社市", " 早島市", " 笠岡市", " 井原市", " 浅口市", " 里庄市", " 矢掛市", " 高梁市", " 新見市", " 真庭市", " 新庄市", " 津山市", " 鏡野町", " 久米南町",  " 美咲町", " 美作市"," 勝央町"," 奈義町", " 西栗倉町"]
adv_list = ["大雨", "洪水", "強風", "風雪", "大雪", "波浪", "高潮", "雷", "融雪", "濃霧", "乾燥", "なだれ", "低温", "霜", "着氷", "着雪"]
wrn_list = ["大雨", "洪水", "強風", "暴風雪", "大雪", "波浪", "高潮"]
okayama_info = okayama_.split(',')

print(okayama_info)
print(type(okayama_info))
print(city_list[0])
info = []
element = []
list_okayama = []
i = 0

print(len(city_list))

for list_ in okayama_info:

    if list_ in delete_word:

        okayama_info.remove(list_)
    else:

        list_okayama.append(list_)


for split in city_list:
    element = []
    if 26 == i:
        e = 26
    else:
        e = i + 1
    if split in delete_word:
        pass
    if split in city_list:

        if split == city_list[i]:
            if ' 発表なし' == split:
                element.append(split)
            elif split == city_list[e]:
                pass

            else:
                element.append(split)
        i += 1
        if split == city_list[26]:
            element.append(split)  # この辺に警報系の情報が乗ると思う
        if split in adv_list:
            element.append(split)
        elif split in wrn_list:
            element.append(split)

    info.append(element)




print(info)

links = html.findAll(class_=wrn_)
link = html.findAll(class_=adv_)

for char in links:
    chars = str(char)
    wrn_chars_str.append(chars)

for char in link:
    chars = str(char)
    adv_chars_str.append(chars)

wrn_place = [wrn_chars_str[i:i+7] for i in range(0, len(wrn_chars_str), 7)]
adv_place = [adv_chars_str[i:i+16] for i in range(0, len(adv_chars_str), 16)]


def detailed():
    print('\n警報-------------------------------------------------------------')
    for i, ww in enumerate(wrn_place):
        print(f'{city[i]}{wrn_place[i]}')
    print('\n注意報-----------------------------------------------------------\n')
    for i, ww in enumerate(adv_place):
        print(f'{city[i]}{adv_place[i]}')


def wrn_okayama():
    for count, i in enumerate(wrn_place):
        print(f'====={city[count]}======')
        for con, e in enumerate(i):
            if '<td class="wrn"></td>' == e:
                pass
            elif '<td class="il1"></td>' == e:
                pass
            else:
                print(wrn[con])


def adv_okayama():
    for cou, i in enumerate(adv_place):
        print(f'====={city[cou]}=====')
        for count, e in enumerate(i):
            if '<td class="adv"></td>' == e:
                pass
            elif '<td class="il2"></td>' == e:
                pass
            else:
                print(adv[count])


detailed()
#print('\n==================================================================')
#print('\n+++++警報+++++')
wrn_okayama()
#print('\n+++++注意報+++++')
adv_okayama()
