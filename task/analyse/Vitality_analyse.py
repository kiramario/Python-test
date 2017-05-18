# -*- coding: utf-8 -*-



def analyse_natural(line,stat):
	stat.natural_khid.append(line['khid'])
	if line['cash_value'] != '0':
		stat.natural_cash_kh.append(line['khid'])
	if line['give_value'] != '0':
		stat.natural_givevalue_kh.append(line['khid'])

	
def analyse_affiliation(line,stat):
	stat.affiliation_khid.append(line['khid'])
	if line['cash_value'] != '0':
		stat.affiliation_cash_kh.append(line['khid'])
	if line['give_value'] != '0':
		stat.affiliation_givevalue_kh.append(line['khid'])