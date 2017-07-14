# -*- coding: utf-8 -*-
import datetime,inspect,time

class Logger(object):
	def __init__(self,filename=""):
		self.path = 'C:\\Users\\Administrator\\Desktop\\pythonTest\\task\\log\\'
		if filename == "":
			self.filename = str(datetime.date.today()) + '_task.log'
		else:
			self.filename = filename
	
	def log(self,text='[acupation: no text]'):
		with open(self.path+self.filename, 'ab+') as f:
			f.write(time.strftime("[%H:%M:%S]",time.localtime()) + " : " + text)
			f.write("\r\n")


if __name__ == "__main__":
	l = Logger()
	l.log()