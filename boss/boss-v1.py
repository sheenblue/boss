import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq
import addtodb
browser,page = None,None

async def init():
    global browser,page
    browser = await launch({'headless': False, "userDataDir": r"./cookies",
                            'args': ['--disable-infobars', '--window-size=1920,1080', '--no-sandbox']})  # 关闭无头浏览器
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



async def main():

    await  init()

    url = 'https://www.zhipin.com/web/geek/job?query=%E7%BA%BF%E4%B8%8A%E5%85%BC%E8%81%8C&city=101280600'

    await page.goto(url)  # 跳转
    await asyncio.sleep(10)
    # t = await page.J('.job-card-left')
    t = await page.querySelectorEval('.job-card-left','node => node.href')
    print(t)

    #打开详情页面 job-sec
    await page.goto(t)
    #提取岗位名称
    t1 = '#main > div.job-banner > div > div > div.info-primary > div.name'
    gw = await getxt(t1)



    #职位描述
    t1 = '.job-sec'
    zw = await getxt(t1)

    #公司介绍
    t1 = '.text.fold-text'
    gs = await getxt(t1)
    # 产品介绍
    t1 = '.company-product-intro'
    cp = await getxt(t1)

    #获取公司名称
    t1 = '#main > div.job-box > div > div.job-detail > div.detail-content > div:nth-child(5) > div.name'
    name = await getxt(t1)

    #工商信息
    t1 = '#main > div.job-box > div > div.job-detail > div.detail-content > div:nth-child(5) > div.level-list'
    gsxx = await getxt(t1)

    #公司位置
    t1 = '.location-address'
    wz = await getxt(t1)

    # await asyncio.sleep(50)
    await asyncio.sleep(5)
    await browser.close()  # 关闭

    #输入数据库
    con = addtodb.sql_connection('boss_db')
    t = '(岗位 TEXT, 职位描述 INT, 公司介绍 TEXT, 产品介绍 TEXT, 公司名称 TEXT, 工商信息 TEXT, 公司位置 TEXT)'
    bname = 'bossdb'
    addtodb.create_table(con, bname, t)
    value = (gw,zw,gs,cp,name,gsxx,wz)
    addtodb.sql_insert(con,bname,value)


asyncio.get_event_loop().run_until_complete(main())