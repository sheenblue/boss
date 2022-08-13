# -*- coding: utf-8 -*-
# @Author : sheen
# @Time   : 2022-08-11
# @FILE   : openurl.py

# C:\Users\1111\AppData\Local\pyppeteer\pyppeteer\local-chromium\588429

import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq
import addtodb
import time
import idget

async def main():
    #{'headless':'false','userDataDir':r'./Crashpad/'}
    browser = await launch({'headless': True,"userDataDir":r"D:\hc", 'args': ['--disable-infobars', '--window-size=1920,1080', '--no-sandbox']})  # 关闭无头浏览器
    page = await browser.newPage()


    await page.setViewport({'width': 1920, 'height':1080})

    await page.goto('http://club.roamedit.com/club/?user-create.htm')  # 跳转

    await asyncio.sleep(2)
    #生成邮箱
    email = idget.getmail()
    #生成账号
    name = idget.getid()
    #生成密码

    #数据传入数据库
    con = addtodb.sql_connection('reids')
    t = '(EMAIL TEXT, NAME INT, PASSWORD TEXT)'
    bname = 'reids'
    addtodb.create_table(con,bname,t)
    value = (email,name,name)
    addtodb.sql_insert(con,bname,value)
    #输入邮箱 #email
    await page.type('#email', email)
    #输入账号 #username
    await page.type('#username', name)
    #输入密码 #password
    await page.type('#password', name)

    #点击登录 #submit

    await page.click('#submit', options={
        'button': 'left',
        'clickCount': 1,
        'delay': 300,
    })

    await asyncio.sleep(2)
    #打开投票链接
    #http://club.roamedit.com/club/?thread-2733.htm

    #await page.goto('http://club.roamedit.com/club/?thread-2733.htm')
    await page.goto('http://club.roamedit.com/club/?thread-2737.htm')

    ##body > div > div > div.col-lg-9.main > div:nth-child(3) > div.card-body.pb-0 > div.w-100 > div:nth-child(8) > label > input
    #勾选内容
    n1 = '#body > div > div > div.col-lg-9.main > div:nth-child(3) > div.card-body.pb-0 > div.w-100 > div:nth-child(8) > label > input'
    n2 = '#body > div > div > div.col-lg-9.main > div:nth-child(3) > div.card-body.pb-0 > div.w-100 > div:nth-child(10) > label > input'
    n3 = '#body > div > div > div.col-lg-9.main > div:nth-child(3) > div.card-body.pb-0 > div.w-100 > div:nth-child(3) > label > input'
    n4 = '#body > div > div > div.col-lg-9.main > div:nth-child(3) > div.card-body.pb-0 > div.w-100 > div:nth-child(2) > label > input'
    # await page.click(n1,options={
    #     'button': 'left',
    #     'clickCount': 1,
    #     'delay': 300,
    # })
    # await page.click(n2, options={
    #     'button': 'left',
    #     'clickCount': 1,
    #     'delay': 300,
    # })
    # await page.click(n3, options={
    #     'button': 'left',
    #     'clickCount': 1,
    #     'delay': 300,
    # })
    await page.click(n4, options={
        'button': 'left',
        'clickCount': 1,
        'delay': 300,
    })
    #点击投票
    #a1 = '#body > div > div > div.col-lg-9.main > div:nth-child(3) > div.card-footer.bg-light > a'
    a1 = '.btn.btn-danger.px-5.vote-post-btn'
    await page.click(a1, options={
        'button': 'left',
        'clickCount': 1,
        'delay': 300,
    })
    await asyncio.sleep(2)

    #点击退出
    await page.click(
        '#nav > ul:nth-child(3) > li:nth-child(4) > a',
        options={
            'button': 'left',
            'clickCount': 1,
            'delay': 300,
        })
    print('已退出')




    await asyncio.sleep(5)
    await browser.close()  # 关闭

for i in range(30):
    asyncio.get_event_loop().run_until_complete(main())
##body > div > div > div.col-lg-9.main > div:nth-child(3) > div.card-body.pb-0 > div.w-100 > div:nth-child(2) > label > input