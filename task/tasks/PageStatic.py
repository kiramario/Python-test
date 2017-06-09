# -*- coding: UTF-8 -*-
import urllib,urllib2,json,csv,math,re,datetime,os,time,sys
from task.crawl.crawler import Crawler
import task.analyse.buryDataAnalyse as pageAnalyse
from task.output.outputPageStatic import OutputPageStatic
from Pagestatic_indicator import StatIndication

# 流水数据
class PageStatic(Crawler):
	
	header = [
		('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'),
		('Accept', 'application/json, text/javascript, */*'),
		('Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'),
		('Accept-Encoding', 'gzip, deflate'),
		('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'),
		('X-Requested-With', 'XMLHttpRequest'),
		('Referer', 'http://hxadmin.hx168.com.cn/hxwwz/s/main/data/jg/rawTransactions'),
		('Cookie', 'JSESSIONID=3BB86C6BC2F95066684ACDD6740FAB08; HXTGC=TGC-628-YrVbvkw3DYmhtdQytzgWr9SpewZoR9sgPMz6q3ygEVhtJFBnLS'),
		('Host', 'hxadmin.hx168.com.cn')
	]

	#定义用于统计分析的变量
	stat = StatIndication()
	output = OutputPageStatic()
	
	csvHeaderKeys = []
	
	def __init__(self,data):
		super(PageStatic,self).__init__(PageStatic.header)
		self.data = data
		self.csvHeader = False
		self.pageSize = 2000
		self.itemNo = 1;
		self.csvname="C:\\Users\\Administrator\\Desktop\\" + self.data['p_start'] + "~~" + self.data['p_end'] + ".csv"
		self.requrl = "http://hxadmin.hx168.com.cn/hxwwz/s/commfuncPaging/execute/42000001/json?p_operator=H"
		#计算时间
		begin = datetime.datetime.now()
		self.run()
		end = datetime.datetime.now()
		print "begin: {0}, end: {1}, totalTime: {2}".format(begin,end,end-begin)

	def analseRes(self,resArray):
		for line in resArray:
			if line['event_id'] == '21':	#进入开户页面
				pageAnalyse.analyse_hxaccount(line,PageStatic.stat)
			elif line['event_id'] == '22':	#进入热点页面
				pageAnalyse.analyse_hot_service(line,PageStatic.stat)
			elif line['event_id'] == '27':	#进入热点分享页面
				pageAnalyse.analyse_hot_service_share(line,PageStatic.stat)
			elif line['event_id'] == '23':	#热点解锁
				pageAnalyse.analyse_hot_service_unlock(line,PageStatic.stat)
			elif line['event_id'] == '36':	#业务推送
				pageAnalyse.analyse_recommend(line,PageStatic.stat)
			elif line['event_id'] == '10':	#服务模块1_A点击
				pageAnalyse.analyse_service_1_areaA(line,PageStatic.stat)
			elif line['event_id'] == '11':	#服务模块1_B点击
				pageAnalyse.analyse_service_1_areaB(line,PageStatic.stat)
			elif line['event_id'] == '12':	#服务模块2_A点击
				pageAnalyse.analyse_service_2_areaA(line,PageStatic.stat)
			elif line['event_id'] == '13':	#服务模块2_B点击
				pageAnalyse.analyse_service_2_areaB(line,PageStatic.stat)
			elif line['event_id'] == '14':	#服务模块3_A点击
				pageAnalyse.analyse_service_3_areaA(line,PageStatic.stat)
			elif line['event_id'] == '15':	#服务模块3_B点击
				pageAnalyse.analyse_service_3_areaB(line,PageStatic.stat)

	
			
	def doWriteCsv(self,result):
		writer = csv.writer(file(self.csvname,"ab+"))
		if not self.csvHeader:
			PageStatic.csvHeaderKeys.extend(result[0].keys())
			csvHeaderValues = []
			for headerKey in PageStatic.csvHeaderKeys:
				csvHeaderValues.append(headerKey)
			self.csvHeader = True
			writer.writerow(csvHeaderValues)
		
		for index,line in enumerate(result):
			# self.analseRes(line)
			csvbodyvalue = []
			for headerKey in PageStatic.csvHeaderKeys:
				tdvalue = line[headerKey]
				if headerKey == 'page_url' or headerKey == 'referrer':
					tdvalue = urllib.unquote(line[headerKey])
				csvbodyvalue.append(tdvalue)
			writer.writerow(csvbodyvalue)
			self.itemNo+=1
			
	def outputRes(self):
		text = PageStatic.output.produceText(PageStatic.stat,self.data['p_start'],self.data['p_end'])
		self.writeInText(text,"morningAnalyse")
		
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
				
		for i in range(1, index+1):
			data = self.data.copy()
			data["page.pageNo"] = i
			data['page.pageSize']=self.pageSize
			result = (self.doSearch(self.requrl,data))['results']
			self.analseRes(result)
			self.doWriteCsv(result)
		
		#计算uv,将khid去重
		pageAnalyse.analyse_all_uv(PageStatic.stat)
		self.outputRes()
postData = {"p_start":"2017-06-08","p_end":"2017-06-09"}

s = PageStatic(postData)

