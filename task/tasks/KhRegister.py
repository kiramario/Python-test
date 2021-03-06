﻿# -*- coding:utf-8 -*-
from __future__ import division
import urllib,urllib2,json,datetime,threading,math,Queue
from task.crawl.crawler import Crawler
from task.output.writeCsv import WriteCsv

class KhRegister(Crawler):
	'this is for search all khinfo from kdcc30data..t_cl_kh'
	
	header = [
		('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'),
		('Accept', 'application/json, text/javascript, */*'),
		('Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'),
		('Accept-Encoding', 'gzip, deflate'),
		('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'),
		('X-Requested-With', 'XMLHttpRequest'),
		('Referer', 'http://hxadmin.hx168.com.cn/hxwwz/s/main/weixin/gaoshou/kh_regdetail_yyb'),
		('Cookie', 'JSESSIONID=985B2D149EE2DC48DD2D3DA116C57EDB; HXTGC=TGC-32-YylRVDBRlTK7aMWUBikOMlKVUNUQzOGH2jOZOShy02fGLdWr7i'),
		('Host', 'hxadmin.hx168.com.cn')
	]
	
	def __init__(self,data):
		super(KhRegister,self).__init__(KhRegister.header)
		self.data = data
		self.pageSize = 2000
		self.requrl = "http://hxadmin.hx168.com.cn/hxwwz/s/commfuncPaging/execute/42000003/json?p_operator=IV1"
		csvname = "C:\\Users\\Administrator\\Desktop\\khregister.csv"
		csvheaders=["khid","wxid","phone","createtime","totalcash","leftcash","khzh","khtype","guishujjr_xm","guishu_jjrdm","dwmc","dwbh","khjl","khjlxm","jgmc"]
		self.csv = WriteCsv(csvname,csvheaders)
		self.lock = threading.Lock()
		self.queue = Queue.Queue()
		begin = datetime.datetime.now()
		self.run()
		end = datetime.datetime.now()
		print "begin: {0}, end: {1}, totalTime: {2}".format(begin,end,end-begin)
		
			
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
		threadTaskNum = 20
		loopTime = int(math.ceil(index/threadTaskNum))
		# loopTime=1
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
			
	def mutiple_thread(self,requrl,data):
		result = (self.doSearch(requrl,data))['results']
		self.lock.acquire()
		if len(result) == 0:
			print data["page.pageNo"]
		else:
			self.csv.doWriteCsv(result)
		self.lock.release()


if __name__ == "__main__":
	postData = {}
	khregister = KhRegister(postData)