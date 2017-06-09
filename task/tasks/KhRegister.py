# -*- coding:utf-8 -*-
from __future__ import division
import urllib,urllib2,json,datetime,threading,csv,math
from task.crawl.crawler import Crawler

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
		('Cookie', 'JSESSIONID=3BB86C6BC2F95066684ACDD6740FAB08; HXTGC=TGC-628-YrVbvkw3DYmhtdQytzgWr9SpewZoR9sgPMz6q3ygEVhtJFBnLS'),
		('Host', 'hxadmin.hx168.com.cn')
	]
	
	def __init__(self,data):
		super(KhRegister,self).__init__(KhRegister.header)
		self.data = data
		self.pageSize = 2000
		self.itemNo = 1;
		self.requrl = "http://hxadmin.hx168.com.cn/hxwwz/s/commfunc/execute/98020391/json?operator=B "
		#计算时间
		self.run()

		
		
	def doWriteCsv(self,result):
		csvname = "C:\\Users\\Administrator\\Desktop\\khregister.csv"
		if os.path.exists(csvname):
			try:
				os.remove(csvname)
			except WindowsError, e:
				print u'文件可能被其他程序占用了：message: %s' % e
				time.sleep(1)
				sys.exit(0)
				
		writer = csv.writer(file(csvname,"ab+"))
		csvHeaderKeys = []
		csvHeaderKeys.extend(result[0].keys())
		writer.writerow(csvHeaderKeys)
		
		print csvHeaderKeys
		
		for index,line in enumerate(result):
			csvbodyvalue = []
			for headerKey in csvHeaderKeys:
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
		
		
	def multiple_doSearch(self,requrl,data):
		if not requrl:
			print "[khregister.py]the target url is missing.."
			return
		result = self.doSearch(requrl,data)
		
	def run(self):
		totalIndex = self.getTotalRow()
		begin = datetime.datetime.now()
		
		threadsNum = 2

		loopTime = int(math.ceil(totalIndex / threadsNum))
		# for i in range(loopTime):
		for i in range(1):
			threadsTask = []
			for j in range(1,threadsNum+1):
				index =  j + (i * threadsNum)
				data = self.data.copy()
				data["page.pageNo"] = index
				data['page.pageSize'] = self.pageSize
				# result = (self.doSearch(self.requrl,data))['results']
				
				# t = MyThread(self.doSearch,self.requrl,data)
				t = MyThread(self.multiple_doSearch,self.requrl,data)
				threadsTask.append(t)
				
				
			for t in threadsTask:
				t.start()
			for t in threadsTask:
				t.join()
		
		# for i in range(1, index+1):
		# for i in range(1, 3):
			# data = self.data.copy()
			# data["page.pageNo"] = i
			# data['page.pageSize']=self.pageSize
			# result = (self.doSearch(self.requrl,data))['results']
			# self.doWriteCsv(result)
		# end = datetime.datetime.now()
		print "begin: {0}, end: {1}, totalTime: {2}".format(begin,end,end-begin)
mylock = threading.Lock()	
class MyThread(threading.Thread):
	
	def __init__(self,func,*args):
		super(MyThread,self).__init__()
		self.func = func
		self.args = args
		
	def run(self):
		self.func(self.args[0],self.args[1])
		



if __name__ == "__main__":
	postData = {"dwbh":"-1","resource":"-1"}
	khregister = KhRegister(postData)