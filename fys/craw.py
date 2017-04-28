# -*- coding: UTF-8 -*-

import urllib, urllib2, _winreg, re, os, sys, datetime, zlib,shutil,stat
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
		self.opener = urllib2.build_opener()
		if headers:
			self.opener.addheaders = headers
		
		try:
			responseInfo = self.opener.open(self.request)
			response = responseInfo.read()
			if responseInfo.info().getheader('Content-Encoding'):
				# print responseInfo.info().getheader('Content-Encoding')
				finalresponse = zlib.decompress(response, 16+zlib.MAX_WBITS)
			else:
				finalresponse = response
			self.doWriteIntxt(finalresponse,self.get_desktop() + "\\__kiramriao.txt")
			return finalresponse
		except urllib2.HTTPError,e:
			print 'The server couldn/\'t fulfill the request.'
			print 'Error code: ', e.code 
		except urllib2.URLError,e:
			print e.reason

		
	def doWriteIntxt(self,restring=None, txtfile=None, type=None):
		if not txtfile:
			txtfile = self.get_desktop() + '\\__default_File.txt'
		if restring:
			try:
				if type:
					f = open(txtfile,type)
				else:
					f = open(txtfile,'w')
				f.write(restring)
			except IOError,e:
				print e
			finally:
				f.close()
				
	def makedir(self,dirname):
		if not os.path.exists(dirname):
			os.makedirs(dirname)
		return dirname
		
	def get_desktop(self):
		key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
		return _winreg.QueryValueEx(key, "Desktop")[0]
		
		
class DocCraw(Crawler):
	
	def __init__(self):
		docdir = self.get_desktop() + "\\fanyongsheng\\dochtml"
		self.docdir = docdir
		if os.path.exists(docdir):
			os.chmod(docdir, stat.S_IREAD | stat.S_IWRITE)
			shutil.rmtree(docdir)
		os.mkdir(docdir)

	def analyse(self,results):
		soup = BeautifulSoup(results,'html.parser')
		div = soup.find("div",id="main")

		txtfile = self.docdir + '\\' + self.docname + '.html'
		
		_html = '''<html xmlns="http://www.w3.org/1999/xhtml">
				<head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
				</head><body class="bg3" style="background-color:#f2f2f2">'''
		_html_end = '</body></html>'
		self.doWriteIntxt(_html+unicode(div).encode('utf-8')+_html_end,txtfile)
		
	def run(self,tdInfo):
		url = tdInfo[1]
		self.docname = tdInfo[3]
		results = self.doSearch(url=url,data=None,headers=None)
		self.analyse(results)


class Fanyongsheng(Crawler):
	httpaddr = "http://www.spprec.com"
	searchRes = []
	rootdir = ''
	searchIndex = 1
	StopRun = False
	endDate= ''
	__VIEWSTATE = ''
	#抓取doc
	crawlerdoc = DocCraw()
	def __init__(self):	
		self.rootdir = self.get_desktop() + "\\fanyongsheng"
		self.endDate = raw_input("the end date eg: 2017-04-06 >: ")
		txtfile = self.rootdir + '\\__kirmario.js'
		if os.path.exists(txtfile):
			os.remove(txtfile)
			
		self.doWriteIntxt('var jsarray = [',txtfile,'a+')
		
		begin = datetime.datetime.now()
		
		while True:
			if self.StopRun:
				self.doWriteIntxt('{}]',txtfile,'a+')
				print u"爬取结束"
				end = datetime.datetime.now()
				print u"begin: {0}, end: {1}, consumption time: {2}".format(begin,end, end-begin)
				break
			print u'开始爬取第: ', self.searchIndex, u'页'
			self.run(self.searchIndex)
			self.searchIndex += 1
		
	def wirteJS(self,arr):
		txtfile = self.rootdir + '\\__kirmario.js'
		
		for items in arr:
			str1 = '{name: "' + items[0] + '"'
			str2 =  ', href: "' + items[1] + '"'
			str3 = ', time: "' + items[2] + '"'
			str4 = ', filename: "' + items[3] + '"},'

			self.doWriteIntxt(str1,txtfile,'a+')
			self.doWriteIntxt(str2,txtfile,'a+')
			self.doWriteIntxt(str3,txtfile,'a+')
			self.doWriteIntxt(str4,txtfile,'a+')
	
		Fanyongsheng.searchRes = []
			
	def analyseTd(self,tdTag):
		patTime = re.compile("[\n\r \t]*")
		aTag = tdTag[1].find('a')
		name = (aTag.get_text()).encode("gb18030")	#名称
		time = patTime.sub("",tdTag[2].get_text())	#日期
		href = Fanyongsheng.httpaddr + aTag['href']	#链接
		output = [name,href,time]
		
		#文件名称
		pat = re.compile('InfoID=(.*)&')
		se = pat.search(aTag['href'])
		htmlfilename = se.group(1)
		
		output.append(htmlfilename)
		
		#抓取doc
		Fanyongsheng.crawlerdoc.run(output)

		return output
		
		
	def analyseTr(self, trTag):
		for index, child in enumerate(trTag):
			td = child.find_all("td")
			trInfo = self.analyseTd(td)
			
			
			currentNew = datetime.datetime.strptime(trInfo[2], '%Y-%m-%d')
			endDate = datetime.datetime.strptime(self.endDate, '%Y-%m-%d')
			if endDate > currentNew:
				print "trInfo[2]: " + trInfo[2] + "; self.endDate" + self.endDate
				self.StopRun = True
				break
			Fanyongsheng.searchRes.append(trInfo)
		self.wirteJS(Fanyongsheng.searchRes)

		
	def analyse(self,html_string):
		soup = BeautifulSoup(html_string,'html.parser')
		self.__VIEWSTATE = (soup.find('input', id='__VIEWSTATE'))['value']
		targetHtml = soup.find('table',id="MoreInfoList1_DataGrid1")
		tr = targetHtml.find_all('tr')
		self.analyseTr(tr)

	def run(self,index=None):
		data = {"__VIEWSTATE": self.__VIEWSTATE,"__EVENTTARGET":"MoreInfoList1$Pager","__EVENTARGUMENT":index}
		url = Fanyongsheng.httpaddr + "/sczw/jyfwpt/005001/005001001/MoreInfo.aspx?CategoryNum=005001001"

		headers = [
			('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'),
			('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
			('Accept-Language', 'zh-CN,zh;q=0.8'),
			('Accept-Encoding', 'gzip, deflate'),
			('Content-Type', 'application/x-www-form-urlencoded'),
			('Referer', 'http://www.spprec.com/sczw/jyfwpt/005001/005001001/MoreInfo.aspx?CategoryNum=005001001'),
			('Host', 'www.spprec.com'),
			("Content-Length","11516"),
			("Origin","http://www.spprec.com"),
			("Upgrade-Insecure-Requests","1"),
			("Connection","keep-alive"),
			("Cache-Control","max-age=0")
		]
		results = self.doSearch(url=url,data=data,headers=headers)
		self.analyse(results)
		
f = Fanyongsheng()



