# -*- coding: UTF-8 -*-
import urllib,urllib2,json,csv,math,re,datetime,os,time,sys
from crawler import Crawler
# 金股流水数据
class GoldenStock(Crawler):
	#定义用于统计分析的变量
	stat = {'enterPage':0,'unlock':0,'unlock_noon':0,'unlock_mor':0,'unlockOK':0,'unlockCancel':0,'recharge':0,"articleUnlock":0,
			'1_A_click_m': 0, '1_A_click_n':0, '1_B_click_m': 0, '1_B_click_n': 0, '2_A_click_m': 0, '2_A_click_n': 0, 
			'2_B_click_m': 0, '2_B_click_n': 0, '3_A_click_m': 0, '3_A_click_n': 0, '3_B_click_m': 0,'3_B_click_n': 0
	}
	eventMap = {
		"1": u"进入金股页面",
		"2": u"点击解锁按钮",
		"3": u"点击充值链接",
		"4": u"点击解锁金股确认按钮",
		"5": u"点击解锁金股取消按钮",
		"6": u"积分不足免费获取200积分按钮",
		"7": u"文章解锁",
		"8": u"进入投资计划",
		"9": u"加入投资计划",
		'10': u"服务模块1_A点击",
		"11": u"服务模块1_B点击",
		"12": u"服务模块2_A点击",
		"13": u"服务模块2_B点击",
		"14": u"服务模块3_A点击",
		"15": u"服务模块3_B点击"
	}
	csvheaddict = {
		'screen_width': '屏幕宽度',
		'screen_height': '屏幕高度',
		'event_id': '事件编号',
		'event':'事件名称',
		'channel': 'channel标识',
		'already_handled': '是否处理',
		'totalrows': '总条数',
		'attr': '文章属性',
		'note':'note',
		'create_time': '创建时间',
		'user_agent':'客户端信息',
		'khid': '客户编号',
		'referrer':'来源页面',
		'os': '操作系统',
		'page_url':'页面url'
	}
	csvHeaderKeys = []
	def __init__(self, headers, data, proxy=True):
		super(GoldenStock,self).__init__(headers,proxy)
		self.data = data
		self.csvHeader = False
		self.pageSize = 2000
		self.itemNo = 1;
		self.csvname="C:\\Users\\Administrator\\Desktop\\goldenStock.csv"
		self.requrl = "http://hxadmin.hx168.com.cn/hxwwz/s/commfuncPaging/execute/42000001/json?p_operator=H"
		
		#计算时间
		begin = datetime.datetime.now()
		self.run()
		end = datetime.datetime.now()
		print "begin: {0}, end: {1}, totalTime: {2}".format(begin,end, end-begin)

	def analseRes(self,line):
		id=line['event_id']
		if id == '1':
			GoldenStock.stat['enterPage'] += 1
		elif id == '2':
			GoldenStock.stat['unlock'] += 1
			if line['channel'] == 'mstock_recommend_noon_service':
				GoldenStock.stat['unlock_noon'] += 1
			elif line['channel'] == 'mstock_recommend_service':
				GoldenStock.stat['unlock_mor'] += 1
		elif id == '3':
			GoldenStock.stat['recharge'] += 1
		elif id == '4':
			GoldenStock.stat['unlockOK'] += 1
		elif id == '5':
			GoldenStock.stat['unlockCancel'] += 1
		elif id == '7':
			GoldenStock.stat['articleUnlock'] += 1
		elif id == '10':
			if line['channel'] == 'recommend_noon_message':
				GoldenStock.stat['1_A_click_n'] += 1
			elif line['channel'] == '' and ( urllib.unquote(line['page_url']) == 'http://wx.hx168.com.cn/hxwwz/rest/json/gaoshou/info/param/page/recommend?sd=20170406' or urllib.unquote(line['page_url'])=='http://wx.hx168.com.cn/hxwwz/rest/json/gaoshou/info/param/page/recommend?source=weixin&sd=20170406'):
				GoldenStock.stat['1_A_click_m'] += 1
		# elif id == '11':
			# GoldenStock.stat['1_B_click'] += 1
		# elif id == '12':
			# GoldenStock.stat['2_A_click'] += 1
		# elif id == '13':
			# GoldenStock.stat['2_B_click'] += 1
		# elif id == '14':
			# GoldenStock.stat['3_A_click'] += 1
		# elif id == '15':
			# GoldenStock.stat['3_B_click'] += 1
			
	def doWriteCsv(self,result):
		resultItems = result[0].keys()
		writer = csv.writer(file(self.csvname,"ab+"))
		if not self.csvHeader:
			GoldenStock.csvHeaderKeys.extend(result[0].keys())
			csvHeaderValues = []
			for i in GoldenStock.csvHeaderKeys:
				if GoldenStock.csvheaddict.has_key(i):
					csvHeaderValues.append(self.chinese(GoldenStock.csvheaddict[i]))
			self.csvHeader = True
			writer.writerow(csvHeaderValues)
		
		for index,line in enumerate(result):
			self.analseRes(line)
			csvbodyvalue = []
			for i in GoldenStock.csvHeaderKeys:
				if GoldenStock.csvheaddict.has_key(i):
					tdvalue = line[i]
					if i == 'page_url' or i == 'referrer':
						tdvalue = urllib.unquote(line[i])
					csvbodyvalue.append(tdvalue)
			writer.writerow(csvbodyvalue)
			self.itemNo+=1
			
	def outputRes(self):
		print u"解锁总数: ", GoldenStock.stat['unlock']
		
		print u"解锁取消: ", GoldenStock.stat['unlockCancel']
		print u"解锁确认: ", GoldenStock.stat['unlockOK']
		
		print u"进入金股页面总数: ", GoldenStock.stat['enterPage']
		
		print u"-----------------------早评-------------------------------"
		print u"早评：热点服务1_A点击次数", GoldenStock.stat['1_A_click_m']
		print u"早评：金股解锁：通过热点服务1_A解锁: ", GoldenStock.stat['unlock_mor']
		print u"------------------------午评------------------------------"
		print u"午评：热点服务1_A点击次数", GoldenStock.stat['1_A_click_n']
		print u"午评：金股解锁：通过热点服务1_A解锁: ", GoldenStock.stat['unlock_noon']
		
				
	def getTotalRow(self):
		data = self.data.copy()
		data["page.pageNo"] = 1
		data['page.pageSize'] = 1
		result = self.doSearch(self.requrl,data)
		totalRow = result["totalRow"]
		totalIndex = int((totalRow+self.pageSize)/self.pageSize)
		print u"查询到总流水的记录数：", totalRow
		return totalIndex
		
	def run(self):
		index = self.getTotalRow()
		if os.path.exists(self.csvname):
			try:
				os.remove(self.csvname)
			except WindowsError, e:
				print u'文件可能被其他程序占用了：message: %s' % e
				time.sleep(1)
				sys.exit(0)
				
		for i in range(1, index+1):
			data = self.data.copy()
			data["page.pageNo"] = i
			data['page.pageSize']=self.pageSize
			result = self.doSearch(self.requrl,data)
			self.doWriteCsv(result['results'])
		self.outputRes()

headers = [
	('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'),
	('Accept', 'application/json, text/javascript, */*'),
	('Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'),
	('Accept-Encoding', 'gzip, deflate'),
	('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'),
	('X-Requested-With', 'XMLHttpRequest'),
	('Referer', 'http://hxadmin.hx168.com.cn/hxwwz/s/main/data/jg/rawTransactions'),
	('Cookie', 'JSESSIONID=17CB2D608B923AD735FA6E0130ADECA8; HXTGC=TGC-18-u5kaI2Uqblpwmyck3U0uaJDa8WHfWvlyMh1Wr6jcilnMyduirE'),
	('Host', 'hxadmin.hx168.com.cn')
]
postData = {"p_start":"2017-04-27","p_end":"2017-04-30"}

s = GoldenStock(headers,postData,False)

