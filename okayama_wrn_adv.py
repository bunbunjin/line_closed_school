import requests
from bs4 import BeautifulSoup


#ToDo:気象庁のHPの再スクレイピング（HP）


res = requests.get('https://typhoon.yahoo.co.jp/weather/jp/warn/33/')
html = BeautifulSoup(res.text, "html.parser")
okayama_south = html.find(class_="warnArea_box").find("table").get_text(", ", strip=True)
okayama_nouth = html.find(id="area_6620").find("table").get_text(", ", strip=True)
print(okayama_nouth)

delete_word = ['南部', ' 岡山地域', ' 倉敷地域', ' 井笠地域', ' 高梁地域', ' 東備地域', ' 津山地域', ' 新見地域', ' 真庭地域', ' 勝英地域', ' 北部']
city_south = [" 岡山市", " 玉野市", " 瀬戸内市", " 吉備中央町", " 倉敷市", " 総社市", " 早島町", " 笠岡市", " 井原市", " 浅口市", " 里庄町", " 矢掛町", " 高梁市", " 備前市", " 赤磐市", " 和気町"]
city_nouth = [" 津山市", " 鏡野町", " 久米南町",  " 美咲町",  " 新見市", " 真庭市", " 新庄村", " 美作市", " 勝央町", " 奈義町", " 西粟倉村"]

adv_list = [" 大雨", " 洪水", " 強風", " 風雪", " 大雪", " 波浪", " 高潮", " 雷", " 融雪", " 濃霧", " 乾燥", " なだれ", " 低温", " 霜", " 着氷", " 着雪"]
wrn_list = [" 大雨", " 洪水", " 強風", " 暴風雪", " 大雪", " 波浪", " 高潮"]

south_info = okayama_south.split(',')
nouth_info = okayama_nouth.split(',')

info = []


def roop_south(list_info):
    i = 0
    for split in list_info:
        element = []

        if 14 == i:
            e = 14
        else:
            e = i + 1
        if split in city_south:
            if split == city_south[i]:
                if ' 発表なし' == split:
                    element.append(split)
                else:
                    element.append(split)

            if split in adv_list:
                element.append(split)
            elif split in wrn_list:
                element.append(split)
            i += 1
        if split in wrn_list:
            element.append(split)
            # ToDo: 警報の詳細の後につく「●●+警報」の処理
        if split in adv_list:
            element.append(split)
        else:
            pass
        info.append(element)


def roop_nouth(list_info):
    i = 0
    for split in list_info:
        element = []

        if 10 == i:
            e = 10

        else:
            e = i + 1

        if split in city_nouth:
            if split == city_nouth[i]:
                element.append(split)

            i += 1

        else:
            if split == city_nouth[e]:
                continue
            else:
                # 　ここに新しい分岐が必要(前と後ろのやつを比較する)
                if split in adv_list:
                    element.append(split)
                elif split in wrn_list:
                    element.append(split)
                if split in wrn_list:
                    element.append(split)
                # ToDo: 警報の詳細の後につく「●●+警報」の処理
                if split in adv_list:
                    element.append(split)
        info.append(element)

roop_nouth(nouth_info)
print(info)
