#encoding:utf-8
from win10toast import ToastNotifier
import requests as r
import os 
import time

toaster = ToastNotifier()
toaster.show_toast(u"zuel查分网监控器",
	u"可以查分的时候我会提醒你~", duration=10)

print(u'[NOTICE] 监控开始')	

while True:
	time.sleep(20)
	os.system('cls')
	try:
		print(u'[NOTICE] 登陆中...')
		login_session = r.post('http://stu.znufe.yanzhao.edu.cn/ssxscx.do', {'zjhm':'！此处填写你的证件号码加密后的文本。你可以通过控制台抓包获取！', 'ksbh':''})
		if login_session.text.find(u'登录信息有误,请重新填写') != -1:
			#print(login_session.text)
			print(u'[NOTICE] 登陆失败，信息未录入...')
			continue
		ybb_cookies = login_session.cookies
		print(u'[NOTICE] 登陆成功')		
		login_get_score = r.get('http://stu.znufe.yanzhao.edu.cn/showPreliminaryScoreInfo.do', cookies=ybb_cookies)
		pos = login_get_score.text.find(u'500 - 系统内部错误')
		if pos != -1 or login_get_score.status_code / 100 == 5:
			print(login_get_score.text)
			print(u'[NOTICE] 成绩未录入，20秒后重新登陆(HTTP %d)' % login_get_score.status_code)
		else:
			print(u'[NOTICE] 成绩好像有了！帮你打开浏览器，快去看看！！！')
			print(u'[NOTICE] 成绩信息：')
			print(login_get_score.text)
			os.system('start http://stu.znufe.yanzhao.edu.cn/ssxscx.do')
			toaster.show_toast(u"zuel查分网监控器",
				u"成绩好像有了！快去看看！！", duration=10)
			os.system('pause')
	except KeyboardInterrupt:
		exit()
	except Exception, e:
		print("[ERROR] ", e)
