import requests

url = "https://api.bilibili.com/x/relation/tags"

payload={}
headers = {
  'authority': 'api.bilibili.com',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6,ru;q=0.5',
  'cache-control': 'max-age=0',
  'cookie': 'buvid3=8BFF345A-1F25-8D02-FE6A-F481850F07C139124infoc; _uuid=F75A19A9-F4102-A494-DE6F-6109C6B54FC7140330infoc; buvid4=C7EE91CF-8F75-E270-F505-B2E281F6942841211-022052813-trJb5CIgyf9yzV61kBp0sw%3D%3D; rpdid=|(k|k)Yu|km|0J;uYlJ~u~uRl; i-wanna-go-back=-1; buvid_fp_plain=undefined; DedeUserID=19402718; DedeUserID__ckMd5=1d96bba77eaf62a4; sid=5vi3sl40; fingerprint3=013f529151c6e5e7c7d4717c7f6f9ca5; fingerprint=250950657b9f73d4f4f7a63d78a69f30; SESSDATA=90803e6c%2C1669270530%2C8742a*51; bili_jct=9277a672c036a693ba6d32c2bc1aa6f8; b_ut=5; buvid_fp=c4b830bcdb0a122ee70142a312080071; CURRENT_BLACKGAP=0; blackside_state=0; nostalgia_conf=-1; hit-dyn-v2=1; LIVE_BUVID=AUTO1516539948677474; CURRENT_QUALITY=80; is-2022-channel=1; b_nut=100; PVID=1; innersign=0; b_lsid=FC688EC3_1832A298609; CURRENT_FNVAL=16; bp_video_offset_19402718=704466579043123300',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'none',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
