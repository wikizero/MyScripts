# coding:utf-8
import Tkinter
import psutil
import time
import threading
import re
import requests

class Test:
    def __init__(self):
        self.root = Tkinter.Tk()
        self.canvas = Tkinter.Canvas(self.root)
        self.x, self.y = 0, 0
        self.win_width, self.win_height = 240, 80
        self.send = ''
        self.receive = ''

    def ip_info(self):
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

    def bytes2human(self, n):
        symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
        prefix = {}
        for i, s in enumerate(symbols):
            prefix[s] = 1 << (i + 1) * 10
        for s in reversed(symbols):
            if n >= prefix[s]:
                value = float(n) / prefix[s]
                return '%.1f %s' % (value, s)
        return '%.1f B' %(n)
    
    def poll(self):
        before = psutil.net_io_counters()
        time.sleep(1.5)
        after = psutil.net_io_counters()

        send = self.bytes2human(after.bytes_sent - before.bytes_sent)
        receive = self.bytes2human(after.bytes_recv - before.bytes_recv)
        self.send = send
        self.receive = receive

    def move(self, event):
        new_x = (event.x-self.x)+self.root.winfo_x()
        new_y = (event.y-self.y)+self.root.winfo_y()
        s = "{width}x{height}+".format(width=self.win_width, height=self.win_height) + str(new_x)+"+" + str(new_y)
        self.root.geometry(s)
        # print("s = ", s)
        # print(self.root.winfo_x(), self.root.winfo_y())
        # print(event.x, event.y)
    
    def button_1(self, event):
        self.x, self.y = event.x,event.y
        # print("event.x, event.y = ", event.x, event.y)

    def enter(self, event):
    	print 'enter'
    	self.win_height = 300
    	self.canvas.configure(height=self.win_height)
    	self.root.update()


    def leave(self, event):
    	print 'leave'
        self.win_height = 80
        self.canvas.configure(height=self.win_height)
    	self.root.update()    	

    def main(self):
        self.root.overrideredirect(True)  # 隐藏菜单栏
        # self.root.attributes("-alpha", 0.3)  # 窗口透明度70 %
        self.root.attributes("-alpha", 0.7)  # 窗口透明度60 %
        height = self.root.winfo_screenheight()  
        width = self.root.winfo_screenwidth()  
        self.root.geometry("{width}x{height}+{x}+{y}".format(width=self.win_width, height=self.win_height,x=width-270, y=120))
        self.root.attributes('-topmost', True)

        canvas = self.canvas
        canvas.configure(width=self.win_width)
        canvas.configure(height=self.win_height)
        canvas.configure(bg="#FCFCFC")
        canvas.bind("<B1-Motion>", self.move)
        canvas.bind("<Button-1>", self.button_1)
        canvas.bind("<Enter>", self.enter)
        canvas.bind("<Leave>", self.leave)
        canvas.configure(highlightthickness=0)
        p1 = canvas.create_text(120, 18, text='', fill='black')

        ret = self.ip_info()
        ip, address = ret if ret else ('', '')
        print ip
        print type(address)
        p2 = canvas.create_text(120, 40, text=ip, fill='black')
        p2 = canvas.create_text(120, 62, text=address, fill='black')
        canvas.pack()        
        while True:
            self.poll()
            canvas.itemconfig(p1, text='Send: ' + self.send + '   Recv: '+self.receive)
            self.root.update()

Test().main()

# top window   panel slide up/down
# 搜索关键字。根据pid kill程序
