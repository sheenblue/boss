
#ctop02 支持全部转换，不单单只有headers

import re
import json
def ctp(t):
    with open(t,'r') as f:
        content = f.read()
        #print(content)
        content = eval(repr(content.replace("\\'", ';')))
        #print(content)
    headers = {}
    patt = "'(.+?)'"

    t = re.findall(patt,content)
    #print(t)
    t.remove(t[0])
    #print(t)
    for i in range(len(t)):
        tt = t[i].split(': ')
        tt[1] = tt[1].replace('"', '\'')
        # tt[1] = str(tt[1])
        tt[1] = eval(repr(tt[1]).replace('\\\\', ';'))
        headers[tt[0]] = tt[1]
    #print(headers)
    return headers

if __name__ == '__main__':
    h  = ctp('1.txt')
    print(h)

    #h = {'a': 'Beijing', 'b': 7}
    print(type(h))
    h = json.dumps(h, sort_keys=True, indent=4, separators=(',', ': '))
    print(h)