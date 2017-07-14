# -*- coding:utf-8 -*-
from __future__ import division
import datetime,json,threading,csv,math,Queue
from time import sleep

from task.crawl.crawler import Crawler

dataLine = []
csvfile = file('C:/Users/Administrator/Desktop/zrll.csv', 'rb')
reader = csv.reader(csvfile)
for line in reader:
	#标准包
	data = {'funcNo': '2000001','khjl_bh': "6212732085458",'br_type':'2','type':'3',
				'app_key':'o2o',
				'phone':line[0],
				'name': '',
				'zfphone':'',
				'ordertype':''}
	#商务包	
	# data = {'funcNo': '2000001',
			# 'app_key':'qdo2o',
			# 'type':'5',
			# 'phone':line[0],
			# 'qdbh': 'gpzj0.25',
			# 'source_flag': '1',
			# 'br_type':'2',
			# 'channel_name': '股票专家'	
	# }
	dataLine.append(data)
csvfile.close()


queue = Queue.PriorityQueue()

class O2O(Crawler):
	header = [
		('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'),
		('Accept', 'application/json, text/javascript, */*'),
		('Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'),
		('Accept-Encoding', 'gzip, deflate'),
		('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'),
		('X-Requested-With', 'XMLHttpRequest'),
		('Host', 'hxadmin.hx168.com.cn')
	]
	
	def writeInText(self,text,name='crawlerRes'):
		filename="C:\\Users\\Administrator\\Desktop\\" + name + ".txt"
		file_object = open(filename, 'a')
		try:
			file_object.write(text)
		finally:
			file_object.close()
			
	def __init__(self,dataLine):
		super(O2O,self).__init__(O2O.header)
		
		self.requrl = 'http://wx.hx168.com.cn/m/servlet/json'
		self.exectotalData = 0
		self.data_succ  = 0
		self.data_before_succ = 0
		self.dataLine = dataLine
		self.threadsNum = 20
		self.mylock = threading.Lock()
		
		begin = datetime.datetime.now()
		loopTime = int(math.ceil(len(self.dataLine) / self.threadsNum))
		print loopTime
		print "============"
		for i in range(loopTime):
			self.multiple(i)
		end = datetime.datetime.now()
		print "begin: {0}, end: {1}, totalTime: {2}".format(begin,end,end-begin)
		
	def multiple(self,i):
		global queue
		self.threads = []
		for j in range(self.threadsNum):
			index =  j + (i * self.threadsNum)
			if index > len(self.dataLine) - 1:
				text = str(index) + " OVER \r\n\r\n"
				queue.put((index,text))
				break
			data = dataLine[index]
			
			t = MyThread(self.run,data,index)
			self.threads.append(t)
			# print index
		for t in self.threads:
			t.start()
			
		for t in self.threads:
			t.join()
			
	def run(self,data,index):
		global queue
		text = str(index) + ": " + data['phone']
		res = None
		try:
			res = self.doSearch(self.requrl,data)
		except Exception,e:
			text += " EXCEPTION:\t" + str(e) + "\r\n\r\n"
			
		self.mylock.acquire()
		
		self.exectotalData += 1
		if res is not None:
			if res["results"][0]['errormsg'] == '前置预约成功!':
			# if res['error_info'] == '调用成功':
				self.data_succ += 1
			resTxt = json.dumps(res)
			text += ":\t" + resTxt.decode("unicode-escape") + "\r\n\r\n"
		queue.put((index,text))
		self.mylock.release()
	
class MyThread(threading.Thread):
	def __init__(self,func,*args):
		super(MyThread,self).__init__()
		self.func = func
		self.args = args
		
	def run(self):
		self.func(self.args[0],self.args[1])

o2o = O2O(dataLine)

for i in range(queue.qsize()):
	o2o.writeInText(queue.get()[1],"O2ORES")


print u"总条数: " + str(len(dataLine))
print u"执行条数: " + str(o2o.exectotalData)
print u"运行成功: " + str(o2o.data_succ)



