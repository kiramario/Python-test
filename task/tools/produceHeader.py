# -*- coding: utf-8 -*-
import ConfigParser

class ProduceHeader(object):
	def __init__(self,iniFile=r"C:\Users\Administrator\Desktop\pythonTest\task\resource\taskIni.ini"):
		self.config = ConfigParser.ConfigParser()
		self.config.readfp(open(iniFile))
		
	def produce(self,section):
		headerArr = ['User-Agent','Accept','Accept-Language','Accept-Encoding','Content-Type','X-Requested-With','Referer','Cookie','Host']
		header = [(x,self.config.get(section,x)) for x in headerArr]
		return header


if __name__ == "__main__":
	pass