# -*- coding: UTF-8 -*-
from __future__ import division
import urllib,urllib2,json,math,re,datetime,os,time,threading
from task.crawl.crawler import Crawler

# 流水数据
class ZJ(Crawler):
	'''根据资金账号查khid或者根据khid查绑定资金账号'''
	header = [
		('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'),
		('Accept', 'application/json, text/javascript, */*'),
		('Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'),
		('Accept-Encoding', 'gzip, deflate'),
		('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'),
		('X-Requested-With', 'XMLHttpRequest'),
		('Referer', 'http://hxadmin.hx168.com.cn/hxwwz/s/main/data/jg/rawTransactions'),
		('Cookie', 'JSESSIONID=AC4B15A126B2656A492C3FE7EC58BE69; HXTGC=TGC-90-1Fmr5TIFcnLLp7IMj4RpHs1n1QDOIFVuLAUTeKalIaHjXXcXvn'),
		('Host', 'hxadmin.hx168.com.cn')
	]

	def __init__(self,data):
		super(ZJ,self).__init__(ZJ.header)
		self.data = data
		self.pageSize = 2000
		self.requrl = "http://hxadmin.hx168.com.cn/hxwwz/s/commfunc/execute/42000003/json?p_operator=IV3"
		self.lock = threading.Lock()
		#计算时间
		begin = datetime.datetime.now()
		self.run()
		end = datetime.datetime.now()
		print "begin: {0}, \r\nend: {1} ".format(begin,end)
		print "totalTime: {0}".format((end-begin).total_seconds())

	
	
	def run(self):
		result = (self.doSearch(self.requrl,self.data))['results']
		print result
		
		
if __name__ == "__main__":
	postData = {"p_id":'96491'}
	s = ZJ(postData)


