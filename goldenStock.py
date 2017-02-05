# -*- coding: UTF-8 -*-
import urllib,urllib2,json,csv,math,re,datetime,cookielib

# 金股流水数据
class GoldenStock(object):
	def __init__(self, proxy=True):
		self.enterPage = 0
		self.unlock = 0
		self.unlockOK = 0
		self.unlockCancel = 0
		self.recharge = 0
		self.csvHeader = False
		self.cookie = "JSESSIONID=DC5F2006ED1EA9E5CB954F22931B91C5;HXTGC=TGC-150-MTQQfWdK3Q7KnaOxeOPJDxSvuC04oyTrSZXuEevTXlhozWhYtA"
		self.static = {
		}
		
		if proxy:
			self.proxy = urllib2.ProxyHandler({'http':'127.0.0.1:8888'})
			self.opener = urllib2.build_opener(self.proxy)
		else:
			self.opener = urllib2.build_opener()
		begin = datetime.datetime.now()
		self.run()
		end = datetime.datetime.now()
		print "begin: {0}, end: {1}, totalTime: {2}".format(begin,end, end-begin)
		
	def chinese(self,character):
		if isinstance(character,unicode):
			return character.encode('gb18030')
		else:
			return character.decode('utf-8').encode('gb18030')
		
	
	def login(self, username, password):
		loginurl = "http://hxadmin.hx168.com.cn/hxwwz/sso/login"
		username = username
		password = password
		
	def logout(self, username, password):
		loginurl = "http://hxadmin.hx168.com.cn/hxwwz/sso/login"
		
	def doSearch(self,requrl,data):
		headers = [
			('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'),
			('Accept', 'application/json, text/javascript, */*'),
			('Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'),
			('Accept-Encoding', 'gzip, deflate'),
			('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'),
			('X-Requested-With', 'XMLHttpRequest'),
			('Referer', 'http://hxadmin.hx168.com.cn/hxwwz/s/main/data/jg/rawTransactions'),
			('Cookie', self.cookie),
			('Host', 'hxadmin.hx168.com.cn')
		]
		data_urlencode = urllib.urlencode(data)
		request = urllib2.Request(url=requrl,data=data_urlencode)
		self.opener.addheaders = headers
		response = self.opener.open(request).read()
		res = response.decode('gb18030')
		resJson = json.loads(res)
		return resJson

	def analseRes(self,line):
		event = line['event'].encode('gb18030')
		if event == self.chinese('进入金股页面'):
			self.enterPage += 1
		elif event == self.chinese('点击解锁按钮'):
			self.unlock += 1
		elif event == self.chinese('点击解锁金股确认按钮'):
			self.unlockOK += 1
		elif event == self.chinese('点击解锁金股取消按钮'):
			self.unlockCancel += 1
		elif event == self.chinese('点击充值链接'):
			self.recharge += 1
		else:
			print "unkown event: ",event

	def doWriteCsv(self,result):
		writer = csv.writer(file("C:\\Users\\Administrator\\Desktop\\goldenStock.csv","ab+"))
		if not self.csvHeader:
			self.csvHeader = True
			writer.writerow([self.chinese("序号"),self.chinese("事件名"),self.chinese("导流渠道")])
		
		for index,line in enumerate(result):
			self.analseRes(line)
			writer.writerow([index,line["event"].encode('gb18030'),line["channel"].encode('gb18030')])
			
	def outputRes(self):
		print "unlock: ", self.unlock
		print "enterPage: ", self.enterPage
		print "unlockCancel: ", self.unlockCancel
		print "unlockOK: ", self.unlockOK
		print "recharge: ", self.recharge
		
	def getTotalRow(self):
		requrl = "http://hxadmin.hx168.com.cn/hxwwz/s/commfuncPaging/execute/42000001/json?p_operator=H"
		data = {"p_start":"2017-01-24","p_end":"2017-01-25","page.pageNo":1,"page.pageSize":1}
		result = self.doSearch(requrl,data)
		totalRow = result["totalRow"]
		totalIndex = int((totalRow+2000)/2000)
		print totalRow
		return totalIndex
		
	def run(self):
		index = self.getTotalRow()

		for i in range(1, index+1):
			requrl = "http://hxadmin.hx168.com.cn/hxwwz/s/commfuncPaging/execute/42000001/json?p_operator=H"
			data = {"p_start":"2017-01-24","p_end":"2017-01-25","page.pageNo":i,"page.pageSize":2000}
			result = self.doSearch(requrl,data)
			self.doWriteCsv(result['results'])
		self.outputRes()

s = GoldenStock(False)
# logouturl = "http://hxadmin.hx168.com.cn/hxwwz/sso/logout"


# cookie = cookielib.CookieJar()
# handler = urllib2.HTTPCookieProcessor(cookie)

# opener = urllib2.build_opener(handler)
# headers = [('Cookie', "JSESSIONID=2729847B8D9AF4A7ADE15D13BE8A8429")]
# opener.addheaders = headers
# data = {'username':"732000003",'password':"0925qf",'telNumber':"1"}
# data_urlencode = urllib.urlencode(data)
# request = urllib2.Request(url="http://hxadmin.hx168.com.cn/hxwwz/sso/login",data=data_urlencode)
# opener.open(request)

# headers = [
			# ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'),
			# ('Accept', 'application/json, text/javascript, */*'),
			# ('Accept-Language', 'h-CN,zh;q=0.8'),
			# ('Accept-Encoding', 'gzip, deflate, sdch'),
			# ('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'),
			# ('Cookie',"JSESSIONID=DC5F2006ED1EA9E5CB954F22931B91C5;HXTGC=TGC-150-MTQQfWdK3Q7KnaOxeOPJDxSvuC04oyTrSZXuEevTXlhozWhYtA"),
			# ('Host', 'hxadmin.hx168.com.cn')
		# ]
#1
# opener = urllib2.build_opener()
# request = urllib2.Request(url="http://hxadmin.hx168.com.cn/hxwwz/sso/login")
# opener.open(request)



#2
# cookie = cookielib.CookieJar()
# handler = urllib2.HTTPCookieProcessor(cookie)
# opener = urllib2.build_opener(handler)
# opener.addheaders = headers
# data = {'username':"",'password':"",'telNumber':""}
# data_urlencode = urllib.urlencode(data)
# request = urllib2.Request(url="http://hxadmin.hx168.com.cn/hxwwz/sso/login",data=data_urlencode)
# opener.open(request)

# for item in cookie:
	# print 'Name: ' + item.name
	# print 'Value: ' + item.value
	



# p = re.compile(r'(\w+) (\w+)')
# s = 'i say, hello world'


# def func(m):
    # return m.group(1).title() + ' ' + m.group(2).title()
	
# print p.subn(func, s)



# static = {'enterPage':{}}
# static['enterPage']['total'] = 0
# for i in range(1,10):
	# key = str(i) + '#'
	# static['enterPage'][key] = i
# print static




