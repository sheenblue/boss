import requests
import ctop02
import json
import datetime
import time
def html(url,headers,data):
    #session = requests.Session()
    payload = {}
    proxies = {
        "http": "127.0.0.1:8889",
        "https": "127.0.0.1:8889",
    }

    response = requests.request("GET", url, headers=headers, params=data).json()

    # response.encoding = 'utf-8'
    # # print(response.text)
    # t = response.text
    # t = json.loads(t)
    # # print(t)
    # # print(type(t))
    # h = json.dumps(t,ensure_ascii=False,sort_keys=True, indent=4,separators=(',', ': '))
    # print(h)
    return response

#时间对比
def paretime(t):
    # 格式化时间戳
    the_time = update_time(t)
    the_time = str(the_time)
    # print('最新视频更新时间是,', the_time)

    # 获取当前时间
    newtime = int(time.time())

    newtime = update_time(newtime)
    # print('nowtime',newtime)

    newtime = str(newtime)

    # newtime = '20220909'
    #print('当前时间是，', newtime)
    if the_time == newtime:
        #print('视频是今天更新的')
        return True
    else:
        #print('视频不是今天更新的')
        return False

#时间戳格式化
def update_time(t):
    #t = str(t)
    timeStamp = t
    dateArray = datetime.datetime.fromtimestamp(timeStamp)
    otherStyleTime = dateArray.strftime('%Y%m%d')
    return otherStyleTime

#获取关注的UP的mid
def mid(headers):
    url = "https://api.bilibili.com/x/relation/tag?"
    data = {
        'mid': '19402718',
        'tagid': '399198',
        'pn': '1',
        'ps': '30',
    }
    content = html(url, headers,data)
    content = dict(content)
    # print(type(content))
    # print(content['data'])
    uplist = content['data']
    # print(len(uplist))
    mid = []
    for i in range(len(uplist)):
        # print(content['data'][0]['mid'])
        mid1 = content['data'][i]['mid']
        mid.append(mid1)
    # print(mid)
    return mid

#获取最新作品
def update(headers,mid):
    up = {}
    url = "http://api.bilibili.com/x/space/arc/search"  # 最新投稿
    data = {
            'mid':mid,
            'pn': '1',
            'ps': '20',

        }
    content = html(url, headers, data)
    # print(content)

    aid = content['data']['list']['vlist'][0]['aid'] #最新作品aid
    title = content['data']['list']['vlist'][0]['title'] #最新作品标题
    author = content['data']['list']['vlist'][0]['author'] #UPID
    created = content['data']['list']['vlist'][0]['created'] #更新时间

    up = {
        'author':author,
        'aid':aid,
        'title':title,
        'created':created
    }

    return up

#添加到稍后再看
def add(headers,aid):
    data = {
        'aid': aid,
        'jsonp': 'jsonp',
        'csrf': '9277a672c036a693ba6d32c2bc1aa6f8'
    }
    url = "http://api.bilibili.com/x/v2/history/toview/add"
    response = requests.request("post", url, headers=headers, params=data).json()

def pushwechat(t,key):
    url = f'https://sc.ftqq.com/{key}.send'
    params = {
        'text':'B站关注UP更新情况',
        'desp':t

    }
    res = requests.get(url,params=params)
    print('推送成功')
    return  res


if __name__ == '__main__':
    ups = []
    update_author = ''
    headers = ctop02.ctp('1.txt')

    #得到up的mid
    mid = mid(headers)
    #print(mid)

    #获取最新作品aid
    for i in range(len(mid)):
        up = update(headers,mid[i])
        # print(up)
        times = up['created']

        times = paretime(times)

        # print(times)

        #判断更新时间，若是今天，添加到稍后再看

        if times == True:
            print(up)
            ups.append(up)
            update_author = '  -' + ' ' + f"{up['author']} {up['title']}\n{update_author}"

            aid = up['aid']
            #添加到稍后再看
            add(headers,aid)
    n = len(ups)
    update_up = f'# 今天有{n}位UP更新：' + '\n' + update_author
    txt = update_up
    print(txt)
    sckey = 'SCT130378TSyYyJSpkVH4cfB4JV2JhfSL1'
    pushwechat(txt, sckey)