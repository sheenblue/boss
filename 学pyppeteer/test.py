import asyncio
from pyppeteer import launch

async def main():
    # 使用launch方法调用浏览器，其参数可以传递关键字参数也可以传递字典。
    browser = await launch({'headless': False, 'userDataDir':r'D:\hc','args': ['--disable-infobars', '--window-size=1920,1080', '--no-sandbox']})
    # 打开一个页面
    page = await browser.newPage()
    await page.setViewport({'width': 1920, 'height': 1080})   # 设置页面的大小
    # 打开链接
    await page.goto('http://club.roamedit.com/club/?thread-2733.htm')

    await page.waitForSelector('#nav > ul > li:nth-child(2) > a')

    t = await page.J('#nav > ul > li:nth-child(2) > a')
    print(t)

    await page.click('#nav > ul:nth-child(3) > li:nth-child(2) > a',options={
        'button':'left',
        'clickCount':1,
        'delay':300,
    })



    await asyncio.sleep(5)

    await browser.close()

# 调用
asyncio.get_event_loop().run_until_complete(main())