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


async def main():
    #{'headless':'false','userDataDir':r'./Crashpad/'}
    browser = await launch({'headless': False,"userDataDir":r"D:\hc", 'args': ['--disable-infobars', '--window-size=1920,1080', '--no-sandbox']})  # 关闭无头浏览器
    page = await browser.newPage()


    await page.setViewport({'width': 1920, 'height':1080})
    #await page.goto('http://club.roamedit.com/club/?thread-2733.htm')  # 跳转
    # await page.click(
    #     '#nav > ul:nth-child(3) > li:nth-child(4) > a',
    #     options={
    #         'button': 'left',
    #         'clickCount': 1,
    #         'delay': 300,
    #     })
    # print('已退出')
    #await asyncio.sleep(2)
    await page.goto('http://club.roamedit.com/club/?thread-2733.htm')  # 跳转
    #await page.screenshot({'path': 'example.png'})  # 截图
    selector ='#nav > ul:nth-child(3) > li:nth-child(2) > a'
    await page.waitForSelector(selector)

    await page.click(selector,options={
        'button':'left',
        'clickCount':1,
        'delay':300,
    })
    await asyncio.sleep(2)

    await page.type('#email','76860877@qq.com')
    await page.type('#password','917051409')

    await page.click('#submit',options={
        'button': 'left',
        'clickCount': 1,
        'delay': 300,
    })

    await asyncio.sleep(2)
    await page.goto('http://club.roamedit.com/club/?thread-2733.htm')


    await page.click('#body > div > div > div.col-lg-9.main > div:nth-child(3) > div.card-body.pb-0 > div.w-100 > div:nth-child(7) > label > input', options={
        'button': 'left',
        'clickCount': 1,
        'delay': 300,
    })
    await asyncio.sleep(1)
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


asyncio.get_event_loop().run_until_complete(main())
