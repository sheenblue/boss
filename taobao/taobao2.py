import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq
import addtodb
browser,page = None,None
import datetime
import time
async def init():
    global browser,page
    browser = await launch({'headless': False, "userDataDir": r"./cookies",'args': ['--disable-infobars', '--window-size=1920,1080', '--no-sandbox']})  # 关闭无头浏览器
    page = await browser.newPage()

    await page.setViewport({'width': 1920, 'height': 1080})

async def getxt(t1):
    try:
        # 产品介绍
        await page.waitForSelector(t1, {'timeout': 3000})
        t = await page.querySelectorEval(t1, 'node => node.innerText')
        print(t)
        # t = t.replace('\n','\\n')
        return t
    except Exception as r:
        print(r)
        t = '无'
        return t




#fm-login-id
#fm-login-password

async def main():

    await  init()
    #url = 'https://www.taobao.com/'
    url = "https://cart.taobao.com/cart.htm?spm=a21bo.jianhua.1997525049.1.5af911d9mnsc57&from=mini&ad_id=&am_id=&cm_id=&pm_id=1501036000a02c5c3739"
    await page.goto(url)  # 跳转
    await asyncio.sleep(20)
    #点击购物车
    n0 = '#J_MiniCart > div.site-nav-menu-hd > a > span:nth-child(2)'
    n1 = '#J_Order_s_2214235872491_1 > div.J_ItemHead.shop.clearfix > div > div > label'
    n2 = '#J_SmallSubmit'
    n3 = '#J_Order_s_3002225584_1 > div.J_ItemHead.shop.clearfix > div > div > label'
    n4 = '#submitOrderPC_1 > div > a.go-btn'
    #J_CheckShop_s_907871871_1
    #J_CheckShop_s_3002225584_1



    await page.waitForSelector(n1)
    await page.click(n1, options={
        'button': 'left',
        'clickCount': 1,
        'delay': 300,
    })

    await asyncio.sleep(0.1)
    times = '2022-08-30 00:00:00'
    n4 = '#submitOrderPC_1 > div > a.go-btn'
    n2 = '#J_SmallSubmit'
    n2s = await getxt(n2)
    print('wait for order')

    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        n4s = ''

        # 对比时间，时间到的话就点击结算
        if now > times:
            # 点击结算按钮
            while True:
                try:

                    if n2s == '结 算':
                        await page.click(n2, options={
                            'button': 'left',
                            'clickCount': 1,
                            'delay': 300,
                        })
                        print(f"结算成功，准备提交订单")
                        break
                except:
                    print('还没到点')
                    pass

            # 点击提交订单按钮
            await page.waitForSelector(n4)
            n4s = await getxt(n4)
            while True:
                try:


                    if n4s == '提交订单':

                        await page.click(n4, options={
                            'button': 'left',
                            'clickCount': 1,
                            'delay': 300,
                        })
                        print(f"抢购成功，请尽快付款")
                        break
                except:
                    print(f"再次尝试提交订单")

            time.sleep(0.01)

            if n4s == '提交订单':
                print('抢购完成')
                break







    # await asyncio.sleep(50)
    await asyncio.sleep(30)
    await browser.close()  # 关闭



asyncio.get_event_loop().run_until_complete(main())