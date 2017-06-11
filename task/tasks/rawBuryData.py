# -*- coding: UTF-8 -*-
from __future__ import division
import urllib,urllib2,json,csv,math,datetime,os,time,sys,threading
from task.crawl.crawler import Crawler

# 流水数据
class RawBuryData(Crawler):
	
	header = [
		('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'),
		('Accept', 'application/json, text/javascript, */*'),
		('Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'),
		('Accept-Encoding', 'gzip, deflate'),
		('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'),
		('X-Requested-With', 'XMLHttpRequest'),
		('Referer', 'http://hxadmin.hx168.com.cn/hxwwz/s/main/data/jg/rawTransactions'),
		('Cookie', 'JSESSIONID=6851460A9EECD38B64927AD0CC4FA26A; HXTGC=TGC-5-g1qxhj1aVkxldaUg7urq3NeS4VWZ8yv0siTRjw7ckdk8FyYfEf'),
		('Host', 'hxadmin.hx168.com.cn')
	]
	
	csvHeaderKeys = []
	
	def __init__(self,data):
		super(RawBuryData,self).__init__(RawBuryData.header)
		self.data = data
		self.csvHeader = False
		self.pageSize = 2000
		self.itemNo = 1;
		self.csvname="C:\\Users\\Administrator\\Desktop\\rawTransactions.csv"
		self.requrl = "http://hxadmin.hx168.com.cn/hxwwz/s/commfuncPaging/execute/42000001/json?p_operator=H"
		self.event = threading.Event()
		self.event.set()
		#计算时间
		begin = datetime.datetime.now()
		self.run()
		end = datetime.datetime.now()
		print "begin: {0}, end: {1}, totalTime: {2}".format(begin,end,end-begin)


	
			
	def doWriteCsv(self,result):
		writer = csv.writer(file(self.csvname,"ab+"))
		if not self.csvHeader:
			RawBuryData.csvHeaderKeys.extend(result[0].keys())
			csvHeaderValues = []
			for headerKey in RawBuryData.csvHeaderKeys:
				csvHeaderValues.append(self.chinese(headerKey))
			self.csvHeader = True
			writer.writerow(csvHeaderValues)
		
		for index,line in enumerate(result):
			csvbodyvalue = []
			for headerKey in RawBuryData.csvHeaderKeys:
				tdvalue = self.chinese(line[headerKey])
				if headerKey == 'page_url' or headerKey == 'referrer':
					tdvalue = urllib.unquote(line[headerKey])
				csvbodyvalue.append(tdvalue)
			writer.writerow(csvbodyvalue)
			self.itemNo+=1
			
		
	def getTotalRow(self):
		data = self.data.copy()
		data["page.pageNo"] = 1
		data['page.pageSize'] = 1
		result = self.doSearch(self.requrl,data)
		totalRow = result["totalRow"]
		totalIndex = int((totalRow+self.pageSize)/self.pageSize)
		print u"查询到总流水的记录数：", totalRow
		return totalIndex
		
	def run(self):
		index = self.getTotalRow()
		if os.path.exists(self.csvname):
			try:
				os.remove(self.csvname)
			except WindowsError, e:
				print u'文件可能被其他程序占用了：message: %s' % e
				time.sleep(1)
				sys.exit(0)
		
		threadTaskNum = 2
		index = 4
		loopTime = int(math.ceil(index/threadTaskNum))
		for i in range(loopTime):
			threadsTasks = []
			for j in range(1,threadTaskNum+1):
				data = self.data.copy()
				data["page.pageNo"] = j + (i * threadTaskNum)
				data['page.pageSize']=self.pageSize
				searchT =  threading.Thread(target=self.mutiple_thread,args=(self.requrl,data))
				threadsTasks.append(searchT)
				
			for t in threadsTasks:
				t.start()
				
			for t in threadsTasks:
				t.join()
		# for i in range(1, 4+1):
			# data = self.data.copy()
			# data["page.pageNo"] = i
			# data['page.pageSize']=self.pageSize
			# result = (self.doSearch(self.requrl,data))['results']
			# self.doWriteCsv(result)
			
	def mutiple_thread(self,requrl,data):
		result = (self.doSearch(requrl,data))['results']
		self.event.wait()
		self.event.clear()
		self.doWriteCsv(result)
		self.event.set()


		
		
		
if __name__ == "__main__":
	postData = {"p_end":"2017-06-09"}
	s = RawBuryData(postData)

	
