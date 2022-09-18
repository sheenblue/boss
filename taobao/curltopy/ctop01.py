import re

def ctp(t):
    with open(t,'r') as f:
        content = f.read()
    headers = {}
    patt = "'(.+?)'"

    t = re.findall(patt,content)
    #print(t)
    t.remove(t[0])
    #print(t)
    for i in range(len(t)):
        tt = t[i].split(': ')
        headers[tt[0]] = tt[1]
    #print(headers)
    return headers
