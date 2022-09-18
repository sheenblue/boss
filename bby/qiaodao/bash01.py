#将curl转换成python支持的格式
import requests
import ctop02

def html(url,headers,name):
    payload = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        print(f'{name}签到成功')
    else:
        print(f'{name}签到失败')

#签到52pojie
h1 = ctop02.ctp('1.txt')
name1 = '吾爱'
url1 = 'https://www.52pojie.cn/home.php?mod=task&do=draw&id=2&referer=https%3A%2F%2Fwww.52pojie.cn%2F.%2F%2F'
url = 'https://www.52pojie.cn/home.php?mod=task&do=apply&id=2&referer=%2Fforum.php%3Fmod%3Dforumdisplay%26fid%3D8%26filter%3Dspecialtype%26specialtype%3Dreward%26rewardtype%3D1'
#html(url,h1,name1)

#签到远景
h2 = ctop02.ctp('2.txt')
name2 = '远景'
url2 = 'https://i.pcbeta.com/home.php?mod=task&do=apply&id=149'
html(url2,h2,name2)

#签到imatxt

h3 = ctop02.ctp('3.txt')
name3 = 'imatxt'
url3 = 'https://www.iamtxt.com/e/extend/signin.php'
html(url3,h3,name3)

#签到柠檬

h4 = ctop02.ctp('4.txt')
name4 = '柠檬'
url4 = 'https://lemonhd.org/attendance.php'
html(url4,h4,name4)