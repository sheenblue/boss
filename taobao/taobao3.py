
#在20220830成功运行脚本

import re
import json
import urllib
import pyttsx3
import requests
import time

from prettytable import PrettyTable
import schedule


def html(url,headers):

    payload = {}


    response = requests.request("GET", url, headers=headers, data=payload)

    #print(response.text)
    return response

'''获得购物车信息'''
def buycartinfo(response):
    response_json = re.search('try{var firstData = (.*?);}catch', response.text).group(1)
    response_json = json.loads(response_json)
    user_id = re.search('\|\^taoMainUser:(.*?):\^', response.headers['s_tag']).group(1)
    return response_json, user_id

'''打印表格'''
def printTable(title, items):
    assert isinstance(title, list) and isinstance(items, list), 'title and items should be list...'
    table = PrettyTable(title)
    for item in items: table.add_row(item)
    print(table)
    return table

'''logging'''
def logging(msg, tip='INFO'):
    print(f'[{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())} {tip}]: {msg}')


'''购买商品'''
def buygood(info, user_id,headers):
    # 发送结算请求
    url = 'https://buy.tmall.com/order/confirm_order.htm?spm=a1z0d.6639537.0.0.undefined'

    cart_id, item_id, sku_id, seller_id, cart_params, to_buy_info = info['cart_id'], info['item_id'], info['sku_id'], info['seller_id'], info['cart_params'], info['to_buy_info']
    data = {
        'item': f'{cart_id}_{item_id}_1_{sku_id}_{seller_id}_0_0_0_{cart_params}_{urllib.parse.quote(str(to_buy_info))}__0',
        'buyer_from': 'cart',
        'source_time': ''.join(str(int(time.time() * 1000))),

    }
    response = session.post(url = url, data = data, headers = headers, verify = False)
    order_info = re.search('orderData= (.*?);\n</script>', response.text).group(1)
    with open('1.txt','w',encoding='utf-8') as f:
        f.write(order_info)
    order_info = json.loads(order_info)
    #print('order_info',order_info)

    # 发送提交订单请求
    #token = requests.cookies['_tb_token_']
    token = 'e373ee05e36be'
    endpoint = order_info['endpoint']
    data = order_info['data']
    structure = order_info['hierarchy']['structure']
    hierarchy = order_info['hierarchy']
    linkage = order_info['linkage']
    linkage.pop('url')
    submitref = order_info['data']['submitOrderPC_1']['hidden']['extensionMap']['secretValue']
    sparam1 = order_info['data']['submitOrderPC_1']['hidden']['extensionMap']['sparam1']
    input_charset = order_info['data']['submitOrderPC_1']['hidden']['extensionMap']['input_charset']
    event_submit_do_confirm = order_info['data']['submitOrderPC_1']['hidden']['extensionMap']['event_submit_do_confirm']
    # print('item_id',item_id)
    # print('user_id',user_id)
    # print('submitref',submitref)
    # print('sparam1',sparam1)
    url = f'https://buy.tmall.com/auction/confirm_order.htm?x-itemid={item_id}&x-uid={user_id}&submitref={submitref}&sparam1={sparam1}'
    #print('url',url)
    data_submit = {}
    for key, value in data.items():
        if value.get('submit') == 'true' or value.get('submit'):
            data_submit[key] = value

    data = {
        'action': '/order/multiTerminalSubmitOrderAction',
        '_tb_token_': token,
        'event_submit_do_confirm': '1',
        'praper_alipay_cashier_domain': 'cashierrz54',
        'input_charset': 'utf-8',
        'endpoint': urllib.parse.quote(json.dumps(endpoint)),
        'data': urllib.parse.quote(json.dumps(data_submit)),
        'hierarchy': urllib.parse.quote(json.dumps({"structure": structure})),
        'linkage': urllib.parse.quote(json.dumps(linkage)),

    }
    #print(data)

    response = requests.post(url, data=data, headers=headers)
    #print(response.status_code)
    if response.status_code == 200: return True
    return False



'''运行'''
def run(t,trybuy_interval):

    cart_infos, user_id = t
    # 解析购物车信息
    if not cart_infos['success']:
        raise RuntimeError('获取购物车信息失败, 请尝试删除cookie缓存文件后重新扫码登录')
    if len(cart_infos['list']) == 0:
        raise RuntimeError('购物车是空的, 请在购物车中添加需要抢购的商品')
    good_infos = {}
    for idx, item in enumerate(cart_infos['list']):
        good_info = {
            'title': item['bundles'][0]['orders'][0]['title'],
            'cart_id': item['bundles'][0]['orders'][0]['cartId'],
            'cart_params': item['bundles'][0]['orders'][0]['cartActiveInfo']['cartBcParams'],
            'item_id': item['bundles'][0]['orders'][0]['itemId'],
            'sku_id': item['bundles'][0]['orders'][0]['skuId'],
            'seller_id': item['bundles'][0]['orders'][0]['sellerId'],
            'to_buy_info': item['bundles'][0]['orders'][0]['toBuyInfo'],
        }
        good_infos[str(idx)] = good_info
    # 打印并选择想要抢购的商品信息
    title, items = ['id', 'title'], []
    for key, value in good_infos.items():
        items.append([key, value['title']])
    printTable(title, items)
    #good_id = input('请选择想要抢购的商品编号(例如"0"): ')
    good_id = '0'
    assert good_id in good_infos, '输入的商品编号有误'
    # 根据选择尝试购买商品
    logging(f'正在尝试抢购商品***{good_infos[good_id]["title"]}***')
    while True:
        try:
            is_success = buygood(good_infos[good_id], user_id,headers)
        except Exception as err:
            logging(f'抢购失败, 错误信息如下: \n{err}\n将在{trybuy_interval}秒后重新尝试.')
            is_success = False
        if is_success: break
        time.sleep(trybuy_interval)
    logging(f'抢购***{good_infos[good_id]["title"]}***成功, 已为您自动提交订单, 请尽快前往淘宝完成付款.')
if __name__ == '__main__':
    headers = {
        'authority': 'cart.taobao.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6,ru;q=0.5',
        'cache-control': 'max-age=0',
        'cookie': 'enc=TUwKZ%2B%2BHexwaSrnt0FBJwbe3k4dZDpW26XGWHMMRvTODaGnD1a8VgnCWaguYX0JxlABJ7sQxQIP3UOTBdhr%2B7U7ITLS%2BuZfSCH5iuU7y39agqdQ3B8w%2FCK66%2F5mVvbD4; t=94e7deedd2770a6a96490084a5acfb49; thw=cn; ubn=p; cna=VcUYG4oeBXYCAXjqIvLC7CmU; lgc=tb0521019308; tracknick=tb0521019308; ucn=center; cookie2=14aa7ff7135f52fb50c3a9bc649e0c76; _tb_token_=ebadb317a7e5e; _m_h5_tk=3eacb128a08f56aa9c0c5bdc90c8397c_1662262896281; _m_h5_tk_enc=8c97c825e95cda7cf6e272520de6508c; _samesite_flag_=true; xlly_s=1; sgcookie=E100vpu6KlMJbzwyw2Cgf9%2FoHs7rnrZBYAovHVC89Uhr4epBtxIWth1zNdnIP4Cg%2BZ2LKDO5mgM60ZxIsbml6jOEVdX%2Bdgo2FcxGqaNvvLf8aDM%3D; unb=2206864184650; uc3=nk2=F5RFhSntHtd3%2Bmwz&id2=UUphzOrMFle5V1isAg%3D%3D&lg2=VT5L2FSpMGV7TQ%3D%3D&vt3=F8dCv4fTCcYHmyePyzE%3D; csg=328dc424; cancelledSubSites=empty; cookie17=UUphzOrMFle5V1isAg%3D%3D; dnk=tb0521019308; skt=075a041979724297; existShop=MTY2MjI1NTM1NA%3D%3D; uc4=nk4=0%40FY4O7FQ%2BDXCdFXAD1Bfdai21s20HI2s%3D&id4=0%40U2grF8GEQ9%2B%2BCrmuO1Uu86NRpmN1coUi; _cc_=VFC%2FuZ9ajQ%3D%3D; _l_g_=Ug%3D%3D; sg=805; _nk_=tb0521019308; cookie1=UNk0wiSN2OjaJLbvsCou9R5j3Ds9XG%2BTkIYBj74UCF8%3D; mt=ci=1_1; uc1=cookie14=UoeyDHAnjh69pA%3D%3D&cookie21=V32FPkk%2FhodrpstKNxZRcg%3D%3D&existShop=false&cookie15=W5iHLLyFOGW7aA%3D%3D&cart_m=0&cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&pas=0; l=eB_VjpiRTggtce2SBO5wlurza77tPIRf1sPzaNbMiInca1PFtFt9TNCEeY69Sdtjgt5E2etP0_WjjdnkumzLRdGjL77lt-OH2Cv6Je1..; isg=BJSUQECui1OrFB-Ha9317tSdZdIG7bjXJTUyEy51iZ-jGTdjVvpQZ46TGRGB4fAv; tfstk=cznNBe63_hKa_1ofCkrqYqRZeyUOaHmmbHP3SQHQAkiH9sUgasD5MJV_BvlGLs4G.; mt=ci=1_1; uc1=pas=0&cookie15=UtASsssmOIJ0bQ%3D%3D&cart_m=0&cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&cookie21=V32FPkk%2FhodrpstKNxZRcg%3D%3D&existShop=false&cookie14=UoeyDHAnjhgyyA%3D%3D; ubn=p; ucn=center',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }
    session = requests.Session()
    trybuy_interval = 0.1
    url = "https://cart.taobao.com/cart.htm?spm=a21bo.jianhua.1997525049.1.5af911d9mnsc57&from=mini&ad_id=&am_id=&cm_id=&pm_id=1501036000a02c5c3739"
    response2 = html(url,headers)

    t = buycartinfo(response2)

    #run(t,trybuy_interval)

    schedule.every().day.at("10:00").do(run, t,trybuy_interval)

    while True:
        schedule.run_pending()
        time.sleep(0.5)
        print(123)