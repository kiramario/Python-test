# -*- coding: UTF-8 -*-
import urllib,urllib2,json,csv,math,re,datetime,os
from crawler import Crawler


class point(Crawler):
	stat = {'customPoint':0}
	def __init__(self, headers, data, proxy=True):
		super(point,self).__init__(headers,proxy)
		self.data = data
		self.pageSize = 2000
		self.itemNo = 1;		
		self.requrl = "http://hxadmin.hx168.com.cn/hxwwz/s/commfunc/execute/98020391/json?operator=A"
		
		#计算时间
		begin = datetime.datetime.now()
		self.run()
		end = datetime.datetime.now()
		print "begin: {0}, end: {1}, totalTime: {2}".format(begin,end, end-begin)
		
		
	def getTotalRow(self):
		data = self.data.copy()
		data["page.pageNo"] = 1
		data['page.pageSize'] = 1
		result = self.doSearch(self.requrl,data)
		totalRow = result["totalRow"]
		totalIndex = int((totalRow+self.pageSize)/self.pageSize)
		print u"查询到总流水的记录数：", totalRow
		return totalIndex
	
	def analyse(self, results):
		for index,line in enumerate(results):
			point.stat['customPoint'] += int(line['cash'])
			
	def run(self):
		index = self.getTotalRow();
		for i in range(1,index+1):
			data = self.data.copy()
			data["page.pageNo"] = i
			data['page.pageSize'] = self.pageSize
			result = self.doSearch(self.requrl,data)
			self.analyse(result['results'])
		print 'cash_value total: ', point.stat['customPoint']
		
headers = [
	('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'),
	('Accept', 'application/json, text/javascript, */*'),
	('Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'),
	('Accept-Encoding', 'gzip, deflate'),
	('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'),
	('X-Requested-With', 'XMLHttpRequest'),
	('Referer', 'http://hxadmin.hx168.com.cn/hxwwz/s/main/weixin/gaoshou/kh_cashdetail_yyb'),
	('Cookie', 'JSESSIONID=1085403E279C0B1C3734E3EDAB754654; HXTGC=TGC-205-cdJXTeow4kkehqWEtpOdDbi92hfNeTlMpd002mKzRcz6g96HX5'),
	('Host', 'hxadmin.hx168.com.cn')
]
postData = {"dwbh":"-1","itemid":"-1","jystartdate":"2016-01-01 00:00:00", "jyenddate": '2016-04-01 00:00:00',"zflyjjrdm":'',"resource":'-1'}
p = point(headers,postData,False)


