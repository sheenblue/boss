import requests
import re
from bs4 import BeautifulSoup
import addtodb

def bbyhtml(url):



  payload={}
  headers = {
    'authority': 'tjupt.org',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6,ru;q=0.5',
    'cookie': 'access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJUSlVQVCIsImF1ZCI6IjEyMzcwNiIsImlhdCI6MTY2MjE5MTUyOSwianRpIjoiZTMzN2MxYjktODJjMS00Y2M2LWIxNzQtYWRhZjJjZWQ2NjhiIiwiZXhwIjoxNjY5OTY3NTI5fQ.0FsVsoXgGdOhhPMi6keIq_UOjzoOWq-pxSjPgtHjBp4; _ga=GA1.2.1152727665.1662191531; _gid=GA1.2.1424765325.1662638268',
    'referer': 'https://tjupt.org/torrents.php',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
  }

  response = requests.request("GET", url, headers=headers, data=payload)
  response.encoding = 'utf-8'
  return response.text

def bbyqd(url,answer):



  data={
    #answer=2022-08-29+09%3A04%3A18%2625&submit=%E6%8F%90%E4%BA%A4
      'answer':answer,
      'submit':'%E6%8F%90%E4%BA%A4',
  }
  headers = {
    'authority': 'tjupt.org',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6,ru;q=0.5',
    'cookie': 'access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJUSlVQVCIsImF1ZCI6IjEyMzcwNiIsImlhdCI6MTY2MjE5MTUyOSwianRpIjoiZTMzN2MxYjktODJjMS00Y2M2LWIxNzQtYWRhZjJjZWQ2NjhiIiwiZXhwIjoxNjY5OTY3NTI5fQ.0FsVsoXgGdOhhPMi6keIq_UOjzoOWq-pxSjPgtHjBp4; _ga=GA1.2.1152727665.1662191531; _gid=GA1.2.1424765325.1662638268',
    'referer': 'https://tjupt.org/torrents.php',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
  }

  response = requests.request("post", url, headers=headers, data=data)
  #response.encoding = 'utf-8'
  return response.status_code

def dbhtml(url):




  payload = {}
  headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6,ru;q=0.5',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'bid=2mvywcyc6gg; douban-fav-remind=1; ll="118282"; __utmv=30149280.14626; gr_user_id=0501d6f8-1197-469d-80cb-afce6895bf77; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1662638762%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D2eMdmmK6nPOeCVpkriWDtK-Bul1W3jlo6MnOFVFDrLhdUsMRi-OSNh_cSa7Q6528%26wd%3D%26eqid%3Dd3d95ced00000606000000066319daa5%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.474698133.1655008066.1662383656.1662638763.14; __utmc=30149280; __utmz=30149280.1662638763.14.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; ap_v=0,6.0; _pk_id.100001.8cb4=f55fcb4c66f39c62.1655008064.14.1662638860.1659255711.; __utmb=30149280.6.10.1662638763',
    'Referer': 'https://www.douban.com/search?q=%E4%BA%BA%E7%94%9F%E8%8B%A5%E5%A6%82%E5%88%9D%E8%A7%81',
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

  response = requests.request("GET", url, headers=headers, data=payload)

  response.encoding = 'utf-8'
  return response.text


def vurl(t):
  #keyword = '三国演义'
  t = str(t)
  keyword = t
  url = requests.utils.quote(keyword) #转换编码

  #print(url)
  return url




if __name__ == '__main__':
    while True:
        url = "https://tjupt.org/attendance.php"

        response = bbyhtml(url)

        soup = BeautifulSoup(response, 'lxml')

        names = soup.find_all(name='input')
        print(names)

        print(len(names))
        print(names[0]['value'])

        patt = "'>(.+?)<br>"
        names2 = re.findall(patt,response)
        print(names2)
        print(len(names2))


        #抓取题目图片链接
        captcha = soup.find(class_='captcha')
        img = captcha.find(name='img')['src']

        print('题目：',img)
        #打开数据库
        con = addtodb.sql_connection('picurl')
        t = "(NAME TEXT, URL TEXT)"
        qname = 'picurls'
        addtodb.create_table(con, qname, t)


        #查询数据库，影片是否有存在


        for i in range(len(names2)):
          top = 'name'
          value = names2[i]
          fetchs = addtodb.sql_fetch(con, qname, top,value)
          print(fetchs)
          if fetchs == False:
            sname = vurl(names2[i])
            sname = f'https://www.douban.com/search?cat=1002&q={sname}'
            #sname = vurl('人生若如初见')


            #获取搜索的片子链接
            url2 = sname
            #print(url2)
            response2 = dbhtml(url2)
            #print(response2)
            soup = BeautifulSoup(response2, 'lxml')

            pic = soup.find(class_='pic')
            #print(pic)
            turl = pic.find(name='a')['href']
            #print(turl)


            #获取主图链接
            url3  =  turl


            response3 = dbhtml(url3)

            patt2 = '<img src="(.+?)" title'

            picurl = re.findall(patt2,response3)
            print(picurl)
            picurl = picurl[0].replace('webp','jpg')
            print(picurl)
            value = (names2[i],picurl)
            addtodb.sql_insert(con,qname,value)
          else:
            print(f'{names2[i]}已经存在数据库')
            pass

        #查询题目链接是否在数据库里
        top2 = 'URL'
        q1 = addtodb.sql_fetch(con,qname,top2,img)

        if q1 == False:
            pass
        else:

            print('q1',q1[0][0])

            for i in range(len(names2)):
                if q1[0][0] == names2[i]:
                    index = i
                    break
                else:
                    pass

            print(f'题目答案是{index}')
            print(names[index]['value'])
            value2 = names[index]['value']
            # value2 = str(value2)
            # value2 = value2.split(' ')
            # print(value2)
            # tt = vurl(value2[1])
            # print(tt)
            # tt = value2[0] + '+' + tt
            # print(tt)

            #签到
            #answer=2022-08-29+09%3A04%3A18%2625&submit=%E6%8F%90%E4%BA%A4
            url = f'https://tjupt.org/attendance.php'
            tt = value2
            tp = bbyqd(url,tt)
            print(tp)
            break
