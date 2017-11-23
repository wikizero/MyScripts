# coding:utf-8
import requests
import uniout
import re
from Tkinter import *


def ip_info():
    url = 'http://2017.ip138.com/ic.asp'
    try:
        ret = requests.get(url)
        ret.encoding = 'gb2312'
        text = ret.text
        ip = re.findall(r'\[(.*)\]', text)[0]
        address = re.findall(u'<center>.*：(.*)</center>', text)[0]

    except Exception, e:
        print 'Get ip info catch exception:', e
        return False

    return ip, address

# virtual_memory()
import psutil
# print psutil.test()
s = 1511346816
import time
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(s))  # 计算启动时间、时间戳转当地时间

# disk_usage('/') 磁盘使用情况

def bytes2human(n):
    """
    >>> bytes2human(10000)
    '9.8 K'
    >>> bytes2human(100001221)
    '95.4 M'
    """
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.2f %s' % (value, s)
    return '%.2f B' % (n)


def poll():
    before = psutil.net_io_counters()
    time.sleep(1.5)
    after = psutil.net_io_counters()

    send = bytes2human(after.bytes_sent - before.bytes_sent)
    receive = bytes2human(after.bytes_recv - before.bytes_recv)

    return send, receive

while True:
    send, receive = poll()
    print 'send:',send
    print 'recv:',receive
    print '-'*30