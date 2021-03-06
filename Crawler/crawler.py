﻿# -*- coding: UTF-8 -*-
import urllib,urllib2,json,csv,math,re,datetime,os
						
class Crawler(object):
	def __init__(self,headers=None,proxy=True):
		self.headers = headers
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
		response = self.opener.open(request).read()
		# self.writeInText(response)	#将结果写入txt
		res = response.decode('gb18030')
		resJson = json.loads(res)
		return resJson
		
	def chinese(self,character):
		if isinstance(character,unicode):
			return character.encode('gb2312')
		else:
			return character.decode('utf-8').encode('gb2312')
			
	def writeInText(self,text):
		filename="C:\\Users\\Administrator\\Desktop\\crawlerRes.txt"
		if os.path.exists(filename):
			os.remove(filename)
		file_object = open(filename, 'w')
		try:
			file_object.write(text)
		finally:
			file_object.close()