# -*- coding:utf-8 -*-
from __future__ import division
import urllib,urllib2,json,datetime,threading,csv,math,os
from task.crawl.crawler import Crawler

class KhRegister(Crawler):
	'single thread this is for search all khinfo from kdcc30data..t_cl_kh'
	
	header = [
		('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'),
		('Accept', 'application/json, text/javascript, */*'),
		('Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'),
		('Accept-Encoding', 'gzip, deflate'),
		('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'),
		('X-Requested-With', 'XMLHttpRequest'),
		('Referer', 'http://hxadmin.hx168.com.cn/hxwwz/s/main/weixin/gaoshou/kh_regdetail_yyb'),
		('Cookie', 'JSESSIONID=51E44682559B0DB6A4E5C64995F7EB3E; HXTGC=TGC-628-YrVbvkw3DYmhtdQytzgWr9SpewZoR9sgPMz6q3ygEVhtJFBnLS'),
		('Host', 'hxadmin.hx168.com.cn')
	]
	

	def __init__(self,data):
		super(KhRegister,self).__init__(KhRegister.header)
		self.csvHeader = ["khid","phone","dwmc","wxid","dwbh","khjlxm","hxstatus","tit","createtime","khjl","zflyjjrxm","zflyjjrdm","jgmc"]
		self.csvH1 = False
		self.csvH2 = False
		self.csvname1 = "C:\\Users\\Administrator\\Desktop\\khregister_wkh.csv"
		self.csvname2 = "C:\\Users\\Administrator\\Desktop\\khregister_ykh.csv"

		self.data = data
		self.pageSize = 2000
		self.itemNo = 1;
		self.requrl = "http://hxadmin.hx168.com.cn/hxwwz/s/commfunc/execute/98020391/json?operator=B"
		#计算时间
		self.run()

		
		
	def doWriteCsv(self,result):	
		for index,line in enumerate(result):
			if line['zflyjjrdm'] !='':
				if line['hxstatus'] == u'未开户':
					writer = csv.writer(file(self.csvname1,"ab+"))
					if not self.csvH1:
						self.csvH1 = True
						writer.writerow(self.csvHeader)
					csvbodyvalue = []

					for headerKey in self.csvHeader:
						tdvalue = line[headerKey]
						csvbodyvalue.append(tdvalue)
					writer.writerow(csvbodyvalue)

				elif line['hxstatus'] == u'已开户':
					writer = csv.writer(file(self.csvname2,"ab+"))
					if not self.csvH1:
						self.csvH2 = True
						writer.writerow(csvHeaderValues)
					csvbodyvalue = []
					for headerKey in self.csvHeader:
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
		totalIndex = self.getTotalRow()
		begin = datetime.datetime.now()
		for i in range(1, totalIndex+1):
		# for i in range(1, 2):
			data = self.data.copy()
			data["page.pageNo"] = i
			data['page.pageSize']=self.pageSize
			result = (self.doSearch(self.requrl,data))['results']
			self.doWriteCsv(result)
		end = datetime.datetime.now()
		print "begin: {0}, end: {1}, totalTime: {2}".format(begin,end,end-begin)



if __name__ == "__main__":
	postData = {"dwbh":"-1","resource":"-1"}
	khregister = KhRegister(postData)