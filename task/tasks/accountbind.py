# -*- coding:utf-8 -*-
from __future__ import division
import urllib,urllib2,json,datetime,threading,csv,math,os
from task.crawl.crawler import Crawler

class Accountbind(Crawler):
	
	header = [
		('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'),
		('Accept', 'application/json, text/javascript, */*'),
		('Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'),
		('Accept-Encoding', 'gzip, deflate'),
		('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'),
		('X-Requested-With', 'XMLHttpRequest'),
		('Referer', 'http://hxadmin.hx168.com.cn/hxwwz/s/main/data/users/users_bind'),
		('Cookie', 'JSESSIONID=51E44682559B0DB6A4E5C64995F7EB3E; HXTGC=TGC-628-YrVbvkw3DYmhtdQytzgWr9SpewZoR9sgPMz6q3ygEVhtJFBnLS'),
		('Host', 'hxadmin.hx168.com.cn')
	]

	csvHeaderKeys = []
	
	def __init__(self,data):
		super(Accountbind,self).__init__(Accountbind.header)
		self.data = data
		self.csvHeader = False
		self.pageSize = 2000
		self.itemNo = 1;
		self.csvname="C:\\Users\\Administrator\\Desktop\\bind_kh.csv"
		self.requrl = "http://hxadmin.hx168.com.cn/hxwwz/s/commfuncPaging/execute/98020604/json?p_operator=N"
		#计算时间
		begin = datetime.datetime.now()
		self.run()
		end = datetime.datetime.now()
		print "begin: {0}, end: {1}, totalTime: {2}".format(begin,end,end-begin)
	
			
	def doWriteCsv(self,result):
		writer = csv.writer(file(self.csvname,"ab+"))
		if not self.csvHeader:
			Accountbind.csvHeaderKeys.extend(result[0].keys())
			csvHeaderValues = []
			for headerKey in Accountbind.csvHeaderKeys:
				csvHeaderValues.append(headerKey)
			self.csvHeader = True
			writer.writerow(csvHeaderValues)
		
		for index,line in enumerate(result):
			# self.analseRes(line)
			csvbodyvalue = []
			for headerKey in Accountbind.csvHeaderKeys:
				tdvalue = line[headerKey]
				csvbodyvalue.append(tdvalue)
			writer.writerow(csvbodyvalue)

		
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
				
		for i in range(1, index+1):
			data = self.data.copy()
			data["page.pageNo"] = i
			data['page.pageSize']=self.pageSize
			result = (self.doSearch(self.requrl,data))['results']
			self.doWriteCsv(result)
postData = {}

s = Accountbind(postData)