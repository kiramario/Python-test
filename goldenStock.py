# -*- coding: UTF-8 -*-
import urllib,urllib2,json,csv,math,re,datetime,os


class Crawler(object):
	def __init__(self,headers,proxy=True):
		self.headers = headers
		if proxy:
			self.proxy = urllib2.ProxyHandler({'http':'127.0.0.1:8888'})
			self.opener = urllib2.build_opener(self.proxy)
		else:
			self.opener = urllib2.build_opener()

	def doSearch(self,requrl,data):
		data_urlencode = urllib.urlencode(data)
		request = urllib2.Request(url=requrl,data=data_urlencode)
		self.opener.addheaders = self.headers
		response = self.opener.open(request).read()
		res = response.decode('gb2312')
		resJson = json.loads(res)
		return resJson
		
	def chinese(self,character):
		if isinstance(character,unicode):
			return character.encode('gb2312')
		else:
			return character.decode('utf-8').encode('gb2312')


# 金股流水数据
class GoldenStock(Crawler):
	def __init__(self, headers, proxy=True):
		super(GoldenStock,self).__init__(headers,proxy)
		self.enterPage = 0
		self.unlock = 0
		self.unlockOK = 0
		self.unlockCancel = 0
		self.recharge = 0
		self.csvHeader = False
		self.pageSize = 2000
		self.itemNo = 1;
		self.csvname="C:\\Users\\Administrator\\Desktop\\goldenStock.csv"

		
		begin = datetime.datetime.now()
		self.run()
		end = datetime.datetime.now()
		print "begin: {0}, end: {1}, totalTime: {2}".format(begin,end, end-begin)

	def analseRes(self,line):
		event = line['event']
		if event == u'进入金股页面':
			self.enterPage += 1
		elif event == u'点击解锁按钮':
			self.unlock += 1
		elif event == u'点击解锁金股确认按钮':
			self.unlockOK += 1
		elif event == u'点击解锁金股取消按钮':
			self.unlockCancel += 1
		elif event == u'点击充值链接':
			self.recharge += 1
		else:
			print "unkown event: ",event

	def doWriteCsv(self,result):
		writer = csv.writer(file(self.csvname,"ab+"))
		if not self.csvHeader:
			self.csvHeader = True
			writer.writerow([u"序号",u"事件名",u"导流渠道"])
		
		for index,line in enumerate(result):
			self.analseRes(line)
			writer.writerow([self.itemNo,line["event"],line["channel"]])
			self.itemNo+=1
			
	def outputRes(self):
		print "unlock: ", self.unlock
		print "enterPage: ", self.enterPage
		print "unlockCancel: ", self.unlockCancel
		print "unlockOK: ", self.unlockOK
		print "recharge: ", self.recharge
		
	def getTotalRow(self):
		requrl = "http://hxadmin.hx168.com.cn/hxwwz/s/commfuncPaging/execute/42000001/json?p_operator=H"
		data = {"p_start":"2017-03-13","p_end":"2017-03-14","page.pageNo":1,"page.pageSize":1}
		result = self.doSearch(requrl,data)
		totalRow = result["totalRow"]
		totalIndex = int((totalRow+self.pageSize)/self.pageSize)
		print totalRow
		return totalIndex
		
	def run(self):
		index = self.getTotalRow()
		if os.path.exists(self.csvname):
			os.remove(self.csvname)
		for i in range(1, index+1):
			requrl = "http://hxadmin.hx168.com.cn/hxwwz/s/commfuncPaging/execute/42000001/json?p_operator=H"
			data = {"p_start":"2017-03-13","p_end":"2017-03-14","page.pageNo":i,"page.pageSize":self.pageSize}
			result = self.doSearch(requrl,data)
			self.doWriteCsv(result['results'])
		self.outputRes()

# s = GoldenStock(headers,False)

		
		
		
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


