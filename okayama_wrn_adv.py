import requests
from bs4 import BeautifulSoup


#ToDo:気象庁のHPの再スクレイピング（HP）


res = requests.get('https://typhoon.yahoo.co.jp/weather/jp/warn/33/')
html = BeautifulSoup(res.text, "html.parser")
okayama_ = html.find(class_="warnArea_box").find("table").get_text(", ", strip=True)

delete_word = ['南部', ' 岡山地域', ' 倉敷地域', ' 井笠地域', ' 高梁地域', ' 東備地域', ' 津山地域', ' 新見地域', ' 真庭地域', ' 勝英地域', ' 北部']
city_list = [" 岡山市", " 玉野市", " 瀬戸内市", " 吉備中央町", " 倉敷市", " 総社市", " 早島市", " 笠岡市", " 井原市", " 浅口市", " 里庄市", " 矢掛市", " 高梁市", " 新見市", " 真庭市", " 新庄市", " 備前市", " 赤磐市", " 和気市", " 津山市", " 鏡野町", " 久米南町",  " 美咲町", " 美作市"," 勝央町"," 奈義町", " 西栗倉町"]
adv_list = ["大雨", "洪水", "強風", "風雪", "大雪", "波浪", "高潮", "雷", "融雪", "濃霧", "乾燥", "なだれ", "低温", "霜", "着氷", "着雪"]
wrn_list = ["大雨", "洪水", "強風", "暴風雪", "大雪", "波浪", "高潮"]

okayama_info = okayama_.split(',')

info = []
i = 0
print(okayama_info)
for a in okayama_info:
    print(a)

for split in okayama_info:
    print('-------------------------')
    print(split)

    element = []

    if 26 == i:
        e = 26
    else:
        e = i + 1

    if split in delete_word:
        okayama_info.remove(split)
        continue
    if split in city_list:

        if split == city_list[i]:
            if ' 発表なし' == split:
                element.append(split)
            else:
                element.append(split)
        if split == city_list[26]:
            element.append(split)  # この辺に警報系の情報が乗ると思う
        if split in adv_list:
            element.append(split)
        elif split in wrn_list:
            element.append(split)
        i += 1
    info.append(element)


print(info)

