# -*- coding: UTF-8 -*-
import urllib,urllib2,json,csv,math,re,datetime,os,time 
from task.tools.logger import Logger

class Crawler(object):
	def __init__(self,headers=None,proxy=False):
		self.headers = headers
		self.logger = Logger()
		if proxy:
			self.proxy = urllib2.ProxyHandler({'http':'127.0.0.1:8888'})
			self.opener = urllib2.build_opener(self.proxy)
		else:
			self.opener = urllib2.build_opener()

	def doSearch(self,requrl=None,data=None):
		if not requrl:
			print "the target url is missing.."
		if data:
			data = urllib.urlencode(data)
		request = urllib2.Request(url=requrl,data=data)
		if self.headers:
			self.opener.addheaders = self.headers
			
		response = ''
		try:
			response = self.opener.open(request).read()
		except urllib2.HTTPError, e:
			text =  'The server couldn\'t fulfill the request. Reason: ' + e.reason
			self.logger.log(text)
			return {"results":[],"totalRow":0}
		except urllib2.URLError, e:
			text = 'We failed to reach a server. Reason: ' + e.reason
			self.logger.log(text)
			return {"results":[],"totalRow":0}
		except:
			self.logger.log("unkown error")
			return {"results":[],"totalRow":0}
		else:
			# self.writeInText(response,"rawBurydata")	#将结果写入txt
			res = response.decode('gb18030')
			resJson = json.loads(res)
			return resJson

	def chinese(self,character):
		if isinstance(character,unicode):
			# print "i am in chinese unicode type"
			return character.encode('gb18030')
		else:
			# print "i am in chinese utf-8 type"
			return character.decode('utf-8').encode('gb18030')
			
	def writeInText(self,text,name='crawlerRes'):
		filename="C:\\Users\\Administrator\\Desktop\\" + name + ".txt"
		if os.path.exists(filename):
			os.remove(filename)
		file_object = open(filename, 'a')
		try:
			file_object.write(text)
		finally:
			file_object.close()
			
	def getTotalRow(self):
		data = self.data.copy()
		data["page.pageNo"] = 1
		data['page.pageSize'] = 1
		result = self.doSearch(self.requrl,data)
		totalRow = result["totalRow"]
		totalIndex = int((totalRow+self.pageSize)/self.pageSize)
		print u"查询到总流水: ", totalRow
		return totalIndex
		
		
if __name__ == "__main__":
	#test
	pass