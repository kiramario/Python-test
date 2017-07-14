# -*- coding: UTF-8 -*-
from __future__ import division
import urllib,json,math,re,datetime,os,time,threading,sys
from task.crawl.crawler import Crawler
import task.analyse.buryDataAnalyse as pageAnalyse
from task.output.outputPageStatic import OutputPageStatic
from task.output.writeCsv import WriteCsv
from Pagestatic_indicator import StatIndication
import task.tools as tools

# 流水数据
class PageStatic(Crawler):
	
	#定义用于统计分析的变量
	stat = StatIndication()
	output = OutputPageStatic()
	header = (tools.produceHeader.ProduceHeader()).produce('PageStatic')
	
	def __init__(self,data):
		super(PageStatic,self).__init__(PageStatic.header)
		self.data = data
		self.pageSize = 2000
		self.itemNo = 1;
		csvname="C:\\Users\\Administrator\\Desktop\\" + self.data['p_start'] + "~~" + self.data['p_end'] + ".csv"
		self.csv = WriteCsv(csvname)
		self.requrl = "http://hxadmin.hx168.com.cn/hxwwz/s/commfuncPaging/execute/42000001/json?p_operator=H"
		self.logger = tools.logger.Logger()
		self.lock = threading.Lock()
		#计算时间
		begin = datetime.datetime.now()
		self.run()
		end = datetime.datetime.now()
		print "begin: {0}, \r\nend: {1} ".format(begin,end)
		m, s = divmod(int((end-begin).total_seconds()), 60)
		h, m = divmod(m, 60)
		print ("{3}: {0:02}:{1:02}:{2:02}".format(h, m, s,"totalTime"))

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
			
	def outputRes(self):
		text = PageStatic.output.produceText(PageStatic.stat,self.data['p_start'],self.data['p_end'])
		self.writeInText(text,"morningAnalyse")
		
	def run(self):
		index = self.getTotalRow()
		threadTaskNum = 20
		loopTime = int(math.ceil(index/threadTaskNum))
		# loopTime = 1
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
				
		#计算uv,将khid去重
		pageAnalyse.analyse_all_uv(PageStatic.stat)
		self.outputRes()
	
	
	def wirte_csv(self,result):
		jsonA = result
		for index,line in enumerate(jsonA):
			line["page_url"] = urllib.unquote(line["page_url"])
			line["referrer"] = urllib.unquote(line["referrer"])
		self.csv.doWriteCsv(jsonA)
		
	def mutiple_thread(self,requrl,data):
		result = (self.doSearch(requrl,data))['results']
		self.lock.acquire()
		if len(result) == 0:
			self.logger.log("line " + str(sys._getframe().f_lineno) + " is empty at " + str(data["page.pageNo"]))
		else:
			self.wirte_csv(result)
			self.analseRes(result)
		self.lock.release()
		
		
if __name__ == "__main__":
	postData = {"p_start":"2017-07-13","p_end":"2017-07-14"}
	s = PageStatic(postData)
