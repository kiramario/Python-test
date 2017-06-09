# -*- coding: utf-8 -*-

import csv

filename="C:\\Users\\Administrator\\Desktop\\sql.txt"

dataLine = []
csvfile = file('C:/Users/Administrator/Desktop/o2otestData.csv', 'rb')
reader = csv.reader(csvfile)
file_object = open(filename, 'a')

try:
	text = 'INSERT INTO `t_cl_gpzj_trackbury` VALUES '
	for line in reader:
		text += "('" + line[0] + "','" + line[1] + "','" + line[2] + "','" + line[3] + "','" + line[4] + "','" + line[5] + "','" + line[6] + "','" + line[7] + "','" + line[8] + "','" + line[9] + "','" + line[10] + "','" + line[11] + "','" + line[12] + "','" + line[13] + "'),"
	file_object.write(text)
finally:
	csvfile.close()
	file_object.close()

