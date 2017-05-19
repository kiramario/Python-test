# -*- coding: utf-8 -*-
import datetime,json

from task.crawl.crawler import Crawler

class A(object):
	def __init__(self):
		self.zhuce_total = 0
		self.zhuce_wkh = []
		self.zhuce_ykh = []

class An(object):
	def zhuce_basic(self,line,stat):
		stat.zhuce_total += 1
		if line['hxstatus'] == u'已开户':
			stat.zhuce_ykh .append(line['khid'])
		else:
			stat.zhuce_wkh .append(line['khid'])


class Zhuce(Crawler):
	header = [
		('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'),
		('Accept', 'application/json, text/javascript, */*'),
		('Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'),
		('Accept-Encoding', 'gzip, deflate'),
		('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'),
		('X-Requested-With', 'XMLHttpRequest'),
		('Referer', 'http://hxadmin.hx168.com.cn/hxwwz/s/main/weixin/gaoshou/kh_regdetail_yyb'),
		('Cookie', 'JSESSIONID=C60C8B34D6804E42F67CB413EC9EF322; HXTGC=TGC-7-6xQWpIuOXGfqNhDKWjQrVCpqyRzpc0RaDLDmEc0QdmjmRFgQkF'),
		('Host', 'hxadmin.hx168.com.cn')
	]
	stat = A()
	anM = An()
	
	def __init__(self,data):
		super(Zhuce,self).__init__(Zhuce.header)
		self.data = data
		self.pageSize = 2000
		self.itemNo = 1
		self.requrl = "http://hxadmin.hx168.com.cn/hxwwz/s/commfunc/execute/98020391/json?operator=B"
		#计算时间
		# begin = datetime.datetime.now()
		# self.run()
		# end = datetime.datetime.now()
		# print "begin: {0}, end: {1}, totalTime: {2}".format(begin,end,end-begin)

	def analseRes(self,resArray):
		for line in resArray:
			# self.writeInText((json.dumps(line)).decode('unicode-escape'),'zhuce')
			Zhuce.anM.zhuce_basic(line,Zhuce.stat)

		
	def outputRes(self):
		text = u'注册人数为: ' + str(self.stat.zhuce_total) + "\r\n"
		text += u'已开户 注册人数为: ' + str(len(set(self.stat.zhuce_ykh))) + "\r\n"
		text += u'未开户 注册人数为: ' + str(len(set(self.stat.zhuce_wkh))) + "\r\n"
		print text
		
	# def getTotalRow(self):
		# data = self.data.copy()
		# data["page.pageNo"] = 1
		# data['page.pageSize'] = 1
		# result = self.doSearch(self.requrl,data)
		# totalRow = result["totalRow"]
		# totalIndex = int((totalRow+self.pageSize)/self.pageSize)
		# print u"查询到总流水: ", totalRow
		# return totalIndex
		
	def run(self):
		index = self.getTotalRow()
		for i in range(1, index+1):
			data = self.data.copy()
			data["page.pageNo"] = i
			data['page.pageSize']=self.pageSize
			result = (self.doSearch(self.requrl,data))['results']
			self.analseRes(result)
		# self.outputRes()
		return self.stat
		
		
		
		
			
		
class Page(Crawler):
	header = [
		('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'),
		('Accept', 'application/json, text/javascript, */*'),
		('Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'),
		('Accept-Encoding', 'gzip, deflate'),
		('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'),
		('X-Requested-With', 'XMLHttpRequest'),
		('Referer', 'http://hxadmin.hx168.com.cn/hxwwz/s/main/data/jg/rawTransactions'),
		('Cookie', 'JSESSIONID=C60C8B34D6804E42F67CB413EC9EF322; HXTGC=TGC-7-6xQWpIuOXGfqNhDKWjQrVCpqyRzpc0RaDLDmEc0QdmjmRFgQkF'),
		('Host', 'hxadmin.hx168.com.cn')
	]
	
	def __init__(self,data):
		super(Page,self).__init__(Page.header)
		self.data = data
		self.pageSize = 2000
		self.itemNo = 1
		self.resDict = {}
		self.requrl = "http://hxadmin.hx168.com.cn/hxwwz/s/commfuncPaging/execute/42000001/json?p_operator=H"
		#计算时间
		# begin = datetime.datetime.now()
		# self.run()
		# end = datetime.datetime.now()
		# print "begin: {0}, end: {1}, totalTime: {2}".format(begin,end,end-begin)

	def analseRes(self,resArray):
		for line in resArray:
			# self.writeInText((json.dumps(line)).decode('unicode-escape'))
			key = line['event']
			khid = line['khid']
			if self.resDict.has_key(key):
				self.resDict[key].append(khid)
			else:
				self.resDict[key] = [khid]

		
	def outputRes(self):
		text = u'注册人数为: ' + str(self.stat.zhuce_total) + "\r\n"
		text += u'已开户 注册人数为: ' + str(len(set(self.stat.zhuce_ykh))) + "\r\n"
		text += u'未开户 注册人数为: ' + str(len(set(self.stat.zhuce_wkh))) + "\r\n"
		print text
		
	# def getTotalRow(self):
		# data = self.data.copy()
		# data["page.pageNo"] = 1
		# data['page.pageSize'] = 1
		# result = self.doSearch(self.requrl,data)
		# totalRow = result["totalRow"]
		# totalIndex = int((totalRow+self.pageSize)/self.pageSize)
		# print u"查询到总流水: ", totalRow
		# return totalIndex
		
	def run(self):
		index = self.getTotalRow()
		for i in range(1, index+1):
			data = self.data.copy()
			data["page.pageNo"] = i
			data['page.pageSize']=self.pageSize
			result = (self.doSearch(self.requrl,data))['results']
			self.analseRes(result)
		# self.outputRes()
		# self.writeInText((json.dumps(self.resDict)).decode('unicode-escape'),'page')
		return self.resDict

if __name__ == "__main__":
	postData1 = {"jystartdate":"2017-05-08 00:00:00","jyenddate":"2017-05-09 00:00:00", "zflyjjrdm": "","dwbh":'-1',"resource":"-1"}
	s = Zhuce(postData1)
	zhuce = s.run()

	postData2 = {"p_start":"2017-05-11","p_end":"2017-05-12"}
	p = Page(postData2)
	page = p.run()
	
	# data = None
	# with open('C:\Users\Administrator\Desktop\page.json') as json_file:
		# all_the_text = json_file.read()
		# all_the_text = all_the_text.decode("gb2312")
		# data = json.loads(all_the_text)
		# print data[u'服务模块2_B点击']
	
	kh_resData = {}
	wkh_resData = {}
	
	for khid in zhuce.zhuce_ykh:
		kh_resData[khid] = []
		for (k,v) in page.items():
			if khid in v:
				kh_resData[khid].append(k)
	
	for khid in zhuce.zhuce_wkh:
		wkh_resData[khid] = []
		for (k,v) in page.items():
			if khid in v:
				wkh_resData[khid].append(k)
	
	text =  u"已开户 \r\n"
	# text += (json.dumps(kh_resData)).decode('unicode-escape') + "\r\n"
	
	text += (json.dumps(kh_resData)).decode('unicode-escape') + "\r\n"
	text += u"未开户  \r\n"
	text += (json.dumps(wkh_resData)).decode('unicode-escape') + "\r\n"
	# text += (json.dumps(wkh_resData)).decode('unicode-escape') + "\r\n"		
	
	# print text
	filename="C:\\Users\\Administrator\\Desktop\\zhuceAnalyse.txt"

	with open(filename, 'a') as file:
		file.write(text)