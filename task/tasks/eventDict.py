# -*- coding: UTF-8 -*-

import crawl, json

class EventDict(crawl.crawler.Crawler):
	header = [
		('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'),
		('Accept', 'application/json, text/javascript, */*'),
		('Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'),
		('Accept-Encoding', 'gzip, deflate'),
		('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'),
		('X-Requested-With', 'XMLHttpRequest'),
		('Referer', 'http://hxadmin.hx168.com.cn/hxwwz/s/main/data/jg/manageEventsDict'),
		('Cookie', 'JSESSIONID=12B22E842035303BFF483B801D41DD2E; HXTGC=TGC-5-SS97CIsoTiM3o1m8yUXcva6c8CaassetDLpmHAplUGL7bqGa2V'),
		('Host', 'hxadmin.hx168.com.cn')
	]
	def __init__(self):
		super(EventDict,self).__init__(EventDict.header)
		self.url = "http://hxadmin.hx168.com.cn/hxwwz/s/commfuncPaging/execute/42000001/json?p_operator=J"

	def analyse(self):
		dictRes = self.doSearch(self.url)
		# print type(dictRes['results'])
		eventDict = dict([ (item['dictid'], {"dictname":item['dictname'], "dicttarget":item['dicttarget']}) for item in dictRes['results'] ])
		# print eventDict
		return eventDict
		# serRes = json.dumps()
		# self.writeInText(serRes.decode("unicode-escape"),"kiramairo_esr")