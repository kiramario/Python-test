# -*- coding: UTF-8 -*-
import csv,os,time,sys


class WriteCsv(object):
	def __init__(self,csvName,csvHeaderKeys=[]):
		self.csvName = csvName
		self.csvHeaderKeys = csvHeaderKeys
		self.headerFlag=True
		if os.path.exists(self.csvName):
			try:
				os.remove(self.csvName)
			except WindowsError, e:
				print u'文件可能被其他程序占用了：message: %s' % e
				time.sleep(1)
				sys.exit(0)
				
		
	def doWriteCsv(self,result):
		with open(self.csvName,"ab+") as f:
			writer = csv.writer(f)
			if self.headerFlag:
				if len(self.csvHeaderKeys) == 0:
					self.csvHeaderKeys.extend(result[0].keys())
					csvHeaderValues = []
					for headerKey in self.csvHeaderKeys:
						csvHeaderValues.append(headerKey)
					self.headerFlag = False
					writer.writerow(csvHeaderValues)
					
			for index,line in enumerate(result):
				csvbodyvalue = []
				for headerKey in self.csvHeaderKeys:
					tdvalue = line[headerKey]
					csvbodyvalue.append(tdvalue)
				writer.writerow(csvbodyvalue)