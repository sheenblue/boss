#生成邮箱，账号名，密码
import random


def getid():
    str = ''
    for i in range(9):
        ch = chr(random.randrange(ord('0'), ord('9') + 1))
        str += ch
    return  str


def getmail():
    str = ''
    for i in range(8):
        ch = chr(random.randrange(ord('0'), ord('9') + 1))
        str += ch

    email = str + '@qq.com'
    return email

if __name__ == '__main__':
    print(getmail())