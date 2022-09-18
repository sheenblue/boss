import requests

url = "https://buy.tmall.com/order/confirm_order.htm?spm=a1z0d.6639537.0.0.undefined"

payload='hex=n&cartId=4310744936057&sellerid=1635636237&cart_param=%7B%22items%22%3A%5B%7B%22cartId%22%3A%224310744936057%22%2C%22itemId%22%3A%22640119465206%22%2C%22skuId%22%3A%224595476960651%22%2C%22quantity%22%3A1%2C%22createTime%22%3A1661264741000%2C%22attr%22%3A%22%3Bop%3A69000%3BcityCode%3A440307%3BitemExtra%3A%7B%7D%3B%22%7D%5D%7D&unbalance=&delCartIds=4310744936057&use_cod=false&buyer_from=cart&page_from=cart&source_time=1661438523032'
headers = {
  'authority': 'buy.tmall.com',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6,ru;q=0.5',
  'cache-control': 'max-age=0',
  'content-type': 'application/x-www-form-urlencoded',
  'cookie': 'dnk=%5Cu90D1%5Cu7076%5Cu534717; uc1=cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&cookie15=VFC%2FuZ9ayeYq2g%3D%3D&cart_m=0&cookie14=UoeyD4YwQvtCDQ%3D%3D&cookie21=VT5L2FSpdeCjwGS%2FFqZpWg%3D%3D&existShop=true&pas=0; uc3=nk2=tehIRR86HZo%3D&lg2=WqG3DMC9VAQiUQ%3D%3D&vt3=F8dCv4fbi04kEHYGZX0%3D&id2=Uonbanu7tckkAA%3D%3D; tracknick=%5Cu90D1%5Cu7076%5Cu534717; lid=%E9%83%91%E7%81%B6%E5%8D%8717; uc4=nk4=0%40t1wCgESThNojtNRZooulfAjywg%3D%3D&id4=0%40UOExPKSdKowesUqIlkBIhMlY76%2FK; _l_g_=Ug%3D%3D; unb=1804386847; lgc=%5Cu90D1%5Cu7076%5Cu534717; cookie1=U%2BHEsGoxErlVzc08hjfRDC2BFJU4g1wKtUO8KWkziKw%3D; login=true; cookie17=Uonbanu7tckkAA%3D%3D; cookie2=1703272154a2f3a222bdfd59c6803249; _nk_=%5Cu90D1%5Cu7076%5Cu534717; sgcookie=E100vHA4VR6taH6sCsyNMetz24tGAMR%2Bt%2B0CD0mUVDZXWhTNVLmiWyeyX691zfThHESmYR1eT7HEcQvyQeOy1zmI%2BCi9YFHR2p4ogS%2BHBzMMdHM%3D; cancelledSubSites=empty; t=94e7deedd2770a6a96490084a5acfb49; sg=776; csg=606463e0; enc=TUwKZ%2B%2BHexwaSrnt0FBJwbe3k4dZDpW26XGWHMMRvTODaGnD1a8VgnCWaguYX0JxlABJ7sQxQIP3UOTBdhr%2B7U7ITLS%2BuZfSCH5iuU7y39agqdQ3B8w%2FCK66%2F5mVvbD4; _tb_token_=5ee7e8ed937e8; cna=VcUYG4oeBXYCAXjqIvLC7CmU; xlly_s=1; isg=BBAQzqjzR5RDnBuQyiD-R4B44V5i2fQjyZk2LwrjJGsxRbDvsumNs2U0HQ2llaz7; ubn=p; ucn=unsh',
  'origin': 'https://cart.taobao.com',
  'referer': 'https://cart.taobao.com/',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'cross-site',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
