# -*- coding: utf-8 -*-
# @Author : sheen
# @Time   : 2022-08-12
# @FILE   : 91zsw.py

import requests
from bs4 import BeautifulSoup
import addtodb
from pyquery import PyQuery as pq
import re
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
    #url = "http://trade.zz91.com/productdetails1842536.htm"
    #url = 'http://trade.zz91.com/productdetails1683269.htm'
    #url = 'http://trade.zz91.com/productdetails2097060.htm'
    #url = 'http://trade.zz91.com/productdetails2036197.htm'
    url = 'http://trade.zz91.com/productdetails1987986.htm'

    phone,contact,jyfw,cpm,sl,lx,xh ='','','','','','',''


    soup = html(url)
    #print(soup)
    txt = soup.find(class_='ifm-con')
    #txt = soup.find(class_='ifm-con-p2 clearfix')
    # if txt == []:
    #     txt = soup.find(class_='ifm-con-p clearfix')
    #     print(txt)
    #print(type(txt))
    txt = txt.find_all(name='p')

    for i in range(len(txt)):
        txt4 = txt[i].find(name='span').string
        txt4 = txt4.strip()
        #print(txt4)
        txt4 = str(txt4)
        if txt4 == '移动电话：':
            txt5 = txt[i].find_all(class_='fl')
            #print(txt5[1])
            txt5 = str(txt5[1])
            patt = '\d{11}'
            txt5 = re.findall(patt,txt5)
            print('phone:',txt5)
            phone = txt5[0]
        elif txt4 == '联 系 人：':
            #print(123)
            txt5 = txt[i].find_all(class_='fl')
            txt5 = txt5[1].string

            contact = txt5.strip()
            contact = ''.join(contact.split())
            print('联系人：', contact)
        elif txt4 == '经营范围：' or txt4 == '范    围：':
            #print(123)
            txt5 = txt[i].find_all(class_='fl')
            txt5 = txt5[1].string
            print('经营范围：',txt5.strip())
            jyfw = txt5.strip()



    # 产品名
    txt1 = soup.find(class_='pro-box clearfix')
    txt2 = txt1.find_all(class_='pro-tle')
    #print(txt2)
    txt3 = txt2[0].string
    print('产品名：',txt3.strip())
    cpm = txt3.strip()
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
            t = ''.join(txt3.split())
            print('现货所在地：', t)
            xh = t
        elif txt3.string == '求购类型：' or txt3.string == '供应类型：':
            #print(txt2[i])
            txt3 = str(txt2[i])
            txt3 = txt3.replace('<span class="pro-main-name">求购类型：</span>', '')
            txt3 = txt3.replace('<span class="pro-main-name">供应类型：</span>', '')
            txt3 = txt3.replace('<p>', '')
            txt3 = txt3.replace('</p>', '')
            txt3 = txt3.replace('   ', '')
            #print(txt3)
            t = ''.join(txt3.split())
            print('求购类型：',t)
            lx = t
        elif txt3.string == '求购数量：' or txt3.string == '供应数量：':
            # print(txt2[i])
            txt3 = str(txt2[i])
            txt3 = txt3.replace('<span class="pro-main-name">求购数量：</span>', '')
            txt3 = txt3.replace('<span class="pro-main-name">供应数量：</span>', '')
            txt3 = txt3.replace('<p>', '')
            txt3 = txt3.replace('</p>', '')
            txt3 = txt3.replace('   ', '')
            #print(txt3)
            t = ''.join(txt3.split())
            print('求购数量：',t)
            sl = t

    con = addtodb.sql_connection('91zsw')
    t = '(NAMES TEXT, PHONES INT, JYFWS TEXT, CPMS TEXT, SLS TEXT, LXS TEXT, XHS TEXT)'
    bname = 'zsw'
    addtodb.create_table(con, bname, t)
    value = (contact,phone,jyfw,cpm,sl,lx,xh)
    addtodb.sql_insert(con, bname, value)