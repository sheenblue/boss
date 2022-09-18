
#在20220830成功运行脚本

import re
import json
import urllib
import pyttsx3
import requests
import time
import ctop01
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
    with open('../1.txt', 'w', encoding='utf-8') as f:
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

    # data = {
    #     'action': '/order/multiTerminalSubmitOrderAction',
    #     '_tb_token_': token,
    #     'event_submit_do_confirm': '1',
    #     'praper_alipay_cashier_domain': 'cashierrz54',
    #     'input_charset': 'utf-8',
    #     'endpoint': urllib.parse.quote(json.dumps(endpoint)),
    #     'data': urllib.parse.quote(json.dumps(data_submit)),
    #     'hierarchy': urllib.parse.quote(json.dumps({"structure": structure})),
    #     'linkage': urllib.parse.quote(json.dumps(linkage)),
    #
    # }
    #print(data)

    response = requests.post(url, headers=headers)
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
    good_id = input('请选择想要抢购的商品编号(例如"0"): ')

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
    headers = ctop01.ctp('3.txt')
    session = requests.Session()
    trybuy_interval = 0.1
    url = "https://cart.taobao.com/cart.htm?spm=a21bo.jianhua.1997525049.1.5af911d9mnsc57&from=mini&ad_id=&am_id=&cm_id=&pm_id=1501036000a02c5c3739"
    response2 = html(url,headers)

    t = buycartinfo(response2)

    run(t,trybuy_interval)

