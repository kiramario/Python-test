# -*- coding: utf-8 -*-

import csv

filename="C:\\Users\\Administrator\\Desktop\\sql.txt"

dataLine = []
csvfile = file('C:/Users/Administrator/Desktop/15/2017-06-15~~2017-06-16.csv', 'rb')
reader = csv.reader(csvfile)
file_object = open(filename, 'a')

try:
	text = 'INSERT INTO `t_cl_tj_monthly_golden_stock_transactions` ( screen_width, event_id, already_handled, attr, note,create_time,user_agent,khid,referrer,screen_height,os,channel,page_url) VALUES '
	for line in reader:
		text += "('" + line[0] + "','" + line[1] + "','" + line[2] + "','" + line[4] + "','" + line[5] + "','" + line[6] + "','" + line[7] + "','" + line[8] + "','" + line[9] + "','" + line[11] + "','" + line[12] + "','" + line[14] + "'," + line[15] + "'),"
	file_object.write(text)
finally:
	csvfile.close()
	file_object.close()

