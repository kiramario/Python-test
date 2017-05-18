# -*- coding: utf-8 -*-
import datetime,json

from task.crawl.crawler import Crawler
from VaitalityKh_indicator import VaitalityKh_indicator
import task.analyse.Vitality_analyse as analyse


class ValitaityKh_02_indicator(object):
	def __init__(self):
		self.affiliation_kh = []
		self.natural_kh = []


class ValitaityKh_02(Crawler):
	header = [
		('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'),
		('Accept', 'application/json, text/javascript, */*'),
		('Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'),
		('Accept-Encoding', 'gzip, deflate'),
		('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'),
		('X-Requested-With', 'XMLHttpRequest'),
		('Referer', 'http://hxadmin.hx168.com.cn/hxwwz/s/main/data/staticsData/account/openAccount_kh'),
		('Cookie', 'JSESSIONID=1837DE11E36C31A3EEB17558F92D3D0A; HXTGC=TGC-103-sNl5PbCzudGpfTUrLsvpcyu3UG0HJwDH1MRKndII7zPXzflm7N'),
		('Host', 'hxadmin.hx168.com.cn')
	]

	stat = ValitaityKh_02_indicator()

	def __init__(self,data):
		super(ValitaityKh_02,self).__init__(ValitaityKh_02.header)
		self.data = data
		self.pageSize = 2000
		self.itemNo = 1;
		self.requrl = "http://hxadmin.hx168.com.cn/hxwwz/s/commfuncPaging/execute/42000002/json?p_operator=A"
		#计算时间
		begin = datetime.datetime.now()
		self.data['p_event_id'] = '22'
		self.run()
		self.data['p_event_id'] = '1'
		self.run()
		self.outputRes()
		end = datetime.datetime.now()
		print "begin: {0}, end: {1}, totalTime: {2}".format(begin,end,end-begin)

	def analseRes(self,resArray):
		for line in resArray:
			# self.writeInText((json.dumps(line)).decode('unicode-escape'))
			# raise NameError('HiThere')
			if line['jjr_dm'] == "":
				ValitaityKh_02.stat.natural_kh.append(line['khid'])
			else:
				ValitaityKh_02.stat.affiliation_kh.append(line['khid'])
		
	def outputRes(self):
		text = self.data['p_start'] + "~~~" + self.data['p_end'] + "\r\n\r\n"
		text += u'有归属' + str(len(set(ValitaityKh_02.stat.affiliation_kh))) + '\r\n'
		text += u'自然流量' + str(len(set(ValitaityKh_02.stat.natural_kh))) + '\r\n'
		print text
		
	def getTotalRow(self):
		data = self.data.copy()
		data["page.pageNo"] = 1
		data['page.pageSize'] = 1
		result = self.doSearch(self.requrl,data)
		totalRow = result["totalRow"]
		totalIndex = int((totalRow+self.pageSize)/self.pageSize)
		print u"查询到总流水: ", totalRow
		return totalIndex
		
	def run(self):
		index = self.getTotalRow()
				
		for i in range(1, index+1):
			data = self.data.copy()
			data["page.pageNo"] = i
			data['page.pageSize']=self.pageSize
			result = (self.doSearch(self.requrl,data))['results']
			self.analseRes(result)
		# self.outputRes()
		
if __name__ == "__main__":
	postData = {"p_start":"2017-04-14","p_end":"2017-05-15", "p_khtype":'2'}
	s = ValitaityKh_02(postData)



