# -*- coding: utf-8 -*-
# @Author : sheen
# @Time   : 2022-08-12
# @FILE   : 91zsw.py

import requests
from bs4 import BeautifulSoup
import addtodb

def html(url):

    #url = "http://trade.zz91.com/productdetails1683269.htm"

    payload = {}
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6,ru;q=0.5',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'Hm_lvt_f41f07cad5c54cf66717306958dd62ed=1660289319; Hm_lvt_7e35be5d826a1f50113c8af7eab584bc=1660289459; userid=AXKSRFYenY1660289469489; JSESSIONID=653124C7B7CF439C27FE0DC45D6C2443; sessionid=ms7a5p1e4ayvyw09kanb6tjc61qe5i36; Hm_lpvt_f41f07cad5c54cf66717306958dd62ed=1660290013; Hm_lpvt_7e35be5d826a1f50113c8af7eab584bc=1660290013; JSESSIONID=9EE1C9E2FD10EAEB7A82D5733B24A712',
        'Referer': 'http://trade.zz91.com/trade/s-e59088e68890e58c96e7baa4.html',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


if __name__ == '__main__':
    url = "http://trade.zz91.com/productdetails1842536.htm"
    soup = html(url)
    #print(soup)
    txt = soup.find_all(class_='ifm-con-p2 clearfix')
    for i in range(len(txt)):
        txt4 = txt[i].find(name='span').string
        txt4 = txt4.strip()
        txt4 = str(txt4)
        if txt4 == '移动电话：':
            txt5 = txt[i].find(class_='fl ifm-con-span-r').string


   #  #联系人
   #  txt2 = txt[0].find_all(class_='fl')
   #  txt3 = txt2[1].string
   #  print(txt3.strip())
   #
   #
   #  #移动电话
   #  txt2 = txt[1].find_all(class_='fl ifm-con-span-r')
   #  #print(txt2)
   #  txt3 = txt2[0].string
   #  #print(txt3)
   #  print(txt3.strip())
   #
   #  # 经营范围
   #  txt2 = txt[5].find_all(class_='fl ifm-con-span-r')
   #  # print(txt2)
   #  txt3 = txt2[0].string
   #  print(txt3.strip())
   # # con = addtodb.sql_connection('91zsw')
   #
   #  # 产品名
   #  txt1 = soup.find(class_='pro-box clearfix')
   #  txt2 = txt1.find_all(class_='pro-tle')
   #  #print(txt2)
   #  txt3 = txt2[0].string
   #  print(txt3.strip())

    #求购数量
    txt1 = txt1.find_all(class_='pro-js-main clearfix')


    txt2 = txt1[0].find_all(name='p')

    for i in range(len(txt2)):

        txt3 = txt2[i].find(name='span')

        if txt3.string == '现货所在地：':
            #print(txt2[i])
            txt3 = str(txt2[i])
            txt3 = txt3.replace('<span class="pro-main-name">现货所在地：</span>', '')
            txt3 = txt3.replace('<p>', '')
            txt3 = txt3.replace('</p>', '')
            txt3 = txt3.replace('   ', '')
            #print(txt3)
            print(''.join(txt3.split()))
        elif txt3.string == '求购类型：' or txt3.string == '供应类型：':
            #print(txt2[i])
            txt3 = str(txt2[i])
            txt3 = txt3.replace('<span class="pro-main-name">求购类型：</span>', '')
            txt3 = txt3.replace('<span class="pro-main-name">供应类型：</span>', '')
            txt3 = txt3.replace('<p>', '')
            txt3 = txt3.replace('</p>', '')
            txt3 = txt3.replace('   ', '')
            #print(txt3)
            print(''.join(txt3.split()))
        elif txt3.string == '求购数量：' or txt3.string == '供应数量：':
            # print(txt2[i])
            txt3 = str(txt2[i])
            txt3 = txt3.replace('<span class="pro-main-name">求购数量：</span>', '')
            txt3 = txt3.replace('<span class="pro-main-name">供应数量：</span>', '')
            txt3 = txt3.replace('<p>', '')
            txt3 = txt3.replace('</p>', '')
            txt3 = txt3.replace('   ', '')
            #print(txt3)
            print(''.join(txt3.split()))


