import random
import time
from selenium import webdriver
import sqlite3
import os
import json
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
def str2():
    str = ''
    for i in range(9):
        ch = chr(random.randrange(ord('0'), ord('9') + 1))
        str += ch
    return  str
def str1():
    str = ''
    for i in range(8):
        ch = chr(random.randrange(ord('0'),ord('9') + 1))
        str += ch

    smail = str + '@qq.com'
    return  smail
try:
    #引入数据库
    con = sqlite3.connect("re_user_db.db")
    cur = con.cursor()
    n = 4
    for i in range(n):
        driver = webdriver.Chrome()  # 模拟浏览器打开网站
        driver.maximize_window()  # 将窗口最大化
        driver.get("http://club.roamedit.com/club/?thread-1757.htm")

        d_windows4 = driver.current_window_handle
        print(d_windows4)
        #点击注册
        #//*[@id="nav"]/ul[2]/li[3]/a
        d1 = driver.find_element_by_xpath('//*[@id="nav"]/ul[2]/li[3]/a')
        d1.click()
        time.sleep(1)
        #生成值
        umail = str1()
        username = str2()
        userpd = str2()
        # 3.执行SQL插入操作
        sql = 'INSERT INTO user (usermail,name,password) VALUES (?,?,?)'
        cur.execute(sql, [umail,username,userpd])

        con.commit()
        print('插入数据成功')
        #//*[@id="email"] #输入邮箱
        d2 = driver.find_element_by_xpath('//*[@id="email"]')
        d2.send_keys(umail)
        #//*[@id="username"] 输入用户名
        d3 = driver.find_element_by_xpath('//*[@id="username"]')
        d3.send_keys(username)
        #//*[@id="password"] 输入密码
        d4 = driver.find_element_by_xpath('//*[@id="password"]')
        d4.send_keys(userpd)

        time.sleep(1)
        #//*[@id="submit"] 点击下一步
        d5 = driver.find_element_by_xpath('//*[@id="submit"]')
        d5.click()

        #等待2秒
        time.sleep(2)
        try:
            #点击1 //*[@id="body"]/div/div/div[1]/div[2]/div[1]/div[2]/div[1]/label/input
            #点击2 //*[@id="body"]/div/div/div[1]/div[2]/div[1]/div[2]/div[2]/label/input
            d6 = driver.find_element_by_xpath('//*[@id="body"]/div/div/div[1]/div[2]/div[1]/div[2]/div[2]/label/input')
            d6.click()
            #点击投票 //*[@id="body"]/div/div/div[1]/div[2]/div[2]/a
            d7 = driver.find_element_by_xpath('//*[@id="body"]/div/div/div[1]/div[2]/div[2]/a')
            d7.click()
            time.sleep(2)
            #点击点赞
            #//*[@id="body"]/div/div/div[1]/div[1]/div/div[3]/div[1]/span/button[1]
            d8 = driver.find_element_by_xpath('//*[@id="body"]/div/div/div[1]/div[1]/div/div[3]/div[1]/span/button[1]')
            d8.click()
            time.sleep(2)
            driver.close()
        except:
            driver.close()
        # 4,提交数据库事务


    time.sleep(10)
    driver.close()
except Exception as r:
    tt = '\nerr %s' % (r)
    with open('err.txt', 'a+') as f:
        f.write(tt)
    print('err %s' % (r))
    driver.quit()

finally:

    #5.关闭游标
    if cur:
        cur.close()
    #6.关闭数据库连接
    if con:
        con.close()