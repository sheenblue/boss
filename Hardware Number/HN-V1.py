# -*- coding: utf-8 -*-
import wmi
c = wmi.WMI()
cpuid=''

for cpu in c.Win32_Processor():
        cpuid = cpu.ProcessorId.strip()

print(cpuid)

#写入本地
with open('data.txt','w',encoding='utf-8') as f:
        f.write(cpuid)
        print('写入成功')