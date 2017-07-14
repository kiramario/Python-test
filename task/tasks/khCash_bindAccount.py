# -*- coding: UTF-8 -*-
from __future__ import division
import math,re,datetime,os,time,threading
from task.crawl.crawler import Crawler
from task.output.writeCsv import WriteCsv
from task.tools.logger import Logger

# 流水数据
class BindKH_CASH(Crawler):
	'''查询绑定资金账号用户的情况'''
	header = [
		('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'),
		('Accept', 'application/json, text/javascript, */*'),
		('Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'),
		('Accept-Encoding', 'gzip, deflate'),
		('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'),
		('X-Requested-With', 'XMLHttpRequest'),
		('Referer', 'http://hxadmin.hx168.com.cn/hxwwz/s/main/data/jg/rawTransactions'),
		('Cookie', 'JSESSIONID=E36CC314568113E56A52707F491171B6; HXTGC=TGC-289-z8gEMW13HKAF0k15srX6NN0bV1pDQCs7IlZcH0DBt6IuZFdHBW'),
		('Host', 'hxadmin.hx168.com.cn')
	]
	
	def __init__(self,data):
		super(BindKH_CASH,self).__init__(BindKH_CASH.header)
		self.logger = Logger()
		self.data = data
		self.pageSize = 2000
		self.itemNo = 1;
		csvname="C:\\Users\\Administrator\\Desktop\\zjkh_cash.csv"
		self.csv = WriteCsv(csvname)
		self.requrl = "http://hxadmin.hx168.com.cn/hxwwz/s/commfuncPaging/execute/42000003/json?p_operator=IV1"
		self.lock = threading.Lock()
		#计算时间
		begin = datetime.datetime.now()
		self.run()
		end = datetime.datetime.now()
		print "begin: {0}, \r\nend: {1} ".format(begin,end)
		m, s = divmod((end-begin).total_seconds(), 60)
		h, m = divmod(m, 60)
		print ("{3}: {0:02}:{1:02}:{2:02}".format(h, m, s,"totalTime"))
	
		# print " {0}".format((end-begin).total_seconds())


		
	def run(self):
		index = self.getTotalRow()
		threadTaskNum = 20
		loopTime = 1
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
	
		
	def mutiple_thread(self,requrl,data):
		result = (self.doSearch(requrl,data))['results']
		self.lock.acquire()
		# if len(result) == 0:
			# self.logger.log(str(data["page.pageNo"]) + ': is empty')
		# else:
			# self.csv.doWriteCsv(result)
		self.lock.release()
		
		
if __name__ == "__main__":
	postData = {"p_bstr_b":"1"}
	s = BindKH_CASH(postData)

	

