# -*- coding: utf-8 -*-
import datetime,json

from task.crawl.crawler import Crawler
from VaitalityKh_indicator import VaitalityKh_indicator
import task.analyse.Vitality_analyse as analyse

class ValitaityKh(Crawler):
	header = [
		('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'),
		('Accept', 'application/json, text/javascript, */*'),
		('Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'),
		('Accept-Encoding', 'gzip, deflate'),
		('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'),
		('X-Requested-With', 'XMLHttpRequest'),
		('Referer', 'http://hxadmin.hx168.com.cn/hxwwz/s/main/data/point/users'),
		('Cookie', 'JSESSIONID=1837DE11E36C31A3EEB17558F92D3D0A; HXTGC=TGC-103-sNl5PbCzudGpfTUrLsvpcyu3UG0HJwDH1MRKndII7zPXzflm7N'),
		('Host', 'hxadmin.hx168.com.cn')
	]


	stat = VaitalityKh_indicator()
	
	
	def __init__(self,data):
		super(ValitaityKh,self).__init__(ValitaityKh.header)
		self.data = data
		self.pageSize = 2000
		self.itemNo = 1;
		self.requrl = " http://hxadmin.hx168.com.cn/hxwwz/s/commfuncPaging/execute/98020604/json?p_operator=J"
		#计算时间
		begin = datetime.datetime.now()
		self.run()
		end = datetime.datetime.now()
		print "begin: {0}, end: {1}, totalTime: {2}".format(begin,end,end-begin)

	def analseRes(self,resArray):
		for line in resArray:
			# self.writeInText((json.dumps(line)).decode('unicode-escape'))
			if line['kh_dwmc'] == "" and line['dwmc'] == '':
				analyse.analyse_natural(line,ValitaityKh.stat)
			else:
				analyse.analyse_affiliation(line,ValitaityKh.stat)
		
	def outputRes(self):
		text = self.data['p_start'] + "~~~" + self.data['p_end'] + "\r\n\r\n"
		
		text += u'自然客户: ' + str(len(set(ValitaityKh.stat.natural_khid))) + '\r\n'
		text += u'自然客户 现金' + str(len(set(ValitaityKh.stat.natural_cash_kh))) + '\r\n'
		text += u'自然客户 赠送' + str(len(set(ValitaityKh.stat.natural_givevalue_kh))) + '\r\n'
		
		text += u'有归属客户: ' + str(len(set(ValitaityKh.stat.affiliation_khid))) + '\r\n'
		text += u'有归属客户 现金' + str(len(set(ValitaityKh.stat.affiliation_cash_kh))) + '\r\n'
		text += u'有归属客户 赠送' + str(len(set(ValitaityKh.stat.affiliation_givevalue_kh))) + '\r\n'
		
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
		
		
		
		
		self.outputRes()
		
		



if __name__ == "__main__":
	postData = {"p_start":"2017-04-15","p_end":"2017-05-15", "p_code": "0", "p_ecode":'0',"p_type": '0', "p_idstr":"8,9,13,14,15,17,18,19,20"}
	s = ValitaityKh(postData)



