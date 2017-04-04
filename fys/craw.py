# -*- coding: UTF-8 -*-

import urllib, urllib2, _winreg, re
from bs4 import BeautifulSoup,NavigableString

class Crawler(object):
	request = None
	opener = None
	def __init__(self):
		pass
	
	def doSearch(self,url=None,data=None,headers=None):
		if not url:
			print "no url is designated !!"
			return
		if data:
			data = urllib.urlencode(data)
		self.request = urllib2.Request(url,data)
		if headers:
			self.opener.addheaders = headers
		self.opener = urllib2.build_opener()
		try:
			response = self.opener.open(self.request).read()
			return response
			# self.doWriteIntxt(response)
		except urllib2.HTTPError,e:
			print 'The server couldn/\'t fulfill the request.'
			print 'Error code: ', e.code 
		except urllib2.URLError,e:
			print e.reason

		
	def doWriteIntxt(self,restring=None):
		txtfile = self.get_desktop() + '\\resText.txt'
		if restring:
			try:
				f = open(txtfile,'w+')
				f.write(restring)
			except IOError,e:
				print e
			finally:
				f.close()
		
	def get_desktop(self):
		key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
		return _winreg.QueryValueEx(key, "Desktop")[0]
		
class Fanyongsheng(Crawler):
	httpaddr = "http://www.spprec.com"
	outputstr = ''
	def __init__(self):
		pass
		
	def analyseTd(self,tdTag):
		outputstr = ''
		aTag = tdTag[1].find('a')
		time = tdTag[2].string
		outputstr = outputstr + "----------------"
		outputstr = outputstr + "\r\n" + Fanyongsheng.httpaddr + aTag['href'] + "\r\n"
		outputstr = outputstr + unicode(aTag.string) + "\r\n"
		outputstr = outputstr + unicode(time) + "\r\n"
		return outputstr
		
	def analyseTr(self, trTag):
		for index, child in enumerate(trTag):
			td = child.find_all("td")
			Fanyongsheng.outputstr = Fanyongsheng.outputstr + self.analyseTd(td)
			
		ustr = (Fanyongsheng.outputstr).encode('gb18030')
		self.doWriteIntxt(ustr)
		
	def analyse(self,html_string):
		soup = BeautifulSoup(html_string)
		targetHtml = soup.find('table',id="MoreInfoList1_DataGrid1")
		tr = targetHtml.find_all('tr')
		self.analyseTr(tr)

	def run(self):
		data = {"__VIEWSTATE": '',"__EVENTTARGET":"MoreInfoList1$Pager","__EVENTARGUMENT":'1'}
		url = Fanyongsheng.httpaddr + "/sczw/jyfwpt/005001/005001001/MoreInfo.aspx?CategoryNum=005001001"
		results = self.doSearch(url=url,data=None,headers=None)
		self.analyse(results)
		
f = Fanyongsheng()
f.run()