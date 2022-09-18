import requests

# url = "https://www.52pojie.cn/"
url = "https://www.52pojie.cn/home.php?mod=task&do=apply&id=2&referer=%2Fforum.php%3Fmod%3Dforumdisplay%26fid%3D8%26filter%3Dspecialtype%26specialtype%3Dreward%26rewardtype%3D1"
# url = 'https://www.52pojie.cn/home.php?mod=task&do=draw&id=2&referer=%2Fthread-805784-1-2.html'
def html(url):
  payload = {}
  headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6,ru;q=0.5',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'htVC_2132_connect_is_bind=1; htVC_2132_smile=1D1; KF4=ak1UnU; htVC_2132_saltkey=mjTGLgu5; htVC_2132_lastvisit=1661603325; htVC_2132_auth=bcdbI5HeyUnpQ1eRFOtIpnNHRuyZ5W1Z8eliDaCg%2FnbYWBYfCuBH39%2B9FdO5S%2FP%2FAyv%2FQ%2BavV2OxwUT31i%2FnysTYXjc; htVC_2132_atarget=1; htVC_2132_sid=0; htVC_2132_forum_lastvisit=D_8_1662858442; htVC_2132_visitedfid=16D8D24D2D4; htVC_2132_noticonf=947121D1D3_3_1; htVC_2132_viewid=tid_805784; Hm_lvt_46d556462595ed05e05f009cdafff31a=1662288883,1662819268,1662858182,1662946777; htVC_2132_ulastactivity=1662982556%7C0; htVC_2132_checkpm=1; htVC_2132_st_p=947121%7C1662982588%7Cdd66d4040cbb3ff88739abd17c204025; htVC_2132_lastcheckfeed=947121%7C1662982588; htVC_2132_onlineusernum=21735; htVC_2132_lastact=1662982607%09forum.php%09; Hm_lpvt_46d556462595ed05e05f009cdafff31a=1662982611; htVC_2132_connect_is_bind=1; htVC_2132_lastact=1662982703%09forum.php%09; htVC_2132_sid=0; wzws_sid=1faf225c0bc518480ae6b3628a4677a587a06a0b60acdf7414f995097a2ffea9a6c795c829ab887485d0d3f6e549adb2fe614fec820ea0ee04d05658f818cbd402ab19cd765b7de27f5c1cb6161a0017',
    'Referer': 'https://www.52pojie.cn/thread-805784-1-2.html',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
  }

  response = requests.request("get", url, headers=headers, data=payload)

#print(response.text)
url = 'https://www.52pojie.cn/home.php?mod=task&do=draw&id=2&referer=%2Fthread-805784-1-2.html'
html(url)
url1  = "https://www.52pojie.cn/home.php?mod=task&do=apply&id=2&referer=%2Fforum.php%3Fmod%3Dforumdisplay%26fid%3D8%26filter%3Dspecialtype%26specialtype%3Dreward%26rewardtype%3D1"
html(url1)
url = 'https://www.52pojie.cn/home.php?mod=task&do=draw&id=2&referer=https%3A%2F%2Fwww.52pojie.cn%2F.%2F%2Fforum.php%3Fmod%3Dforumdisplay%26fid%3D8%26filter%3Dspecialtype%26specialtype%3Dreward%26rewardtype%3D1'