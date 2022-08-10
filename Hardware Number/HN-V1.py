# -*- coding: utf-8 -*-
import wmi
import getpass
print(getpass.getuser())#获取用户名

cname = getpass.getuser()

c = wmi.WMI()
cpuid=''
BoardSnid=''
for cpu in c.Win32_Processor():
        cpuid = cpu.ProcessorId.strip()

print(cpuid)
for board_id in c.Win32_BaseBoard():

        BoardSnid = board_id.SerialNumber.strip()
txt = cpuid +'\n' + BoardSnid
#写入本地
with open(f'{cname}.txt','w+',encoding='utf-8') as f:
        f.write(txt)

        print('写入成功')