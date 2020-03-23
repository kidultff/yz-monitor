#encoding:utf-8
from win10toast import ToastNotifier
import requests as r
import os 
import time

toaster = ToastNotifier()
oritxt = r.get('http://yzb2.ustc.edu.cn/cjcx').text
if oritxt.find(u'未开通') == -1:
	print(u'[NOTICE] 可能已经可以查分了，帮你打开浏览器，快去看看')
	os.system('start http://yzb2.ustc.edu.cn/cjcx')
toaster.show_toast(u"USTC查分网监控器",
	u"查分网站内容发生变更时我会通知您，并自动打开浏览器", duration=10)

print(u'[NOTICE] 监控开始')	
while True:
	time.sleep(15)
	os.system('cls')
	print(u'http://yzb2.ustc.edu.cn/cjcx:获取中...')
	try:
		current = r.get('http://yzb2.ustc.edu.cn/cjcx').text
		if current == oritxt:
			print(time.strftime('[NOTICE] %X\tNO...',time.localtime(time.time())))
		else:
			os.system('start http://yzb2.ustc.edu.cn/cjcx')
			toaster.show_toast(u"监控程序",
				u"好像可以查询成绩了，帮你打开浏览器，快去看看", duration=60)
			exit()
	except KeyboardInterrupt:
		exit()
	except Exception, e:
		print("[ERROR] ", e)