# -*- coding: utf-8 -*-


#分析进入热点页面
def analyse_hot_service(line,stat_instance):
	if line['attr'] == '{"id":"2833"}':
		stat_instance.hot_service_pv += 1
		if line['khid'] == '' or line['khid'] == '-1': 
			stat_instance.hot_service_khid_unidentification += 1
		else:
			stat_instance.hot_service_khid.append(line['khid'])

#分析进入分享热点页面
def analyse_hot_service_share(line,stat_instance):
	if line['attr'] == '{"id":"2833"}':
		stat_instance.hot_service_share_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.hot_service_share_khid_unidentification += 1
		else:
			stat_instance.hot_service_share_khid.append(line['khid'])
			
#分析解锁热点
def analyse_hot_service_unlock(line,stat_instance):
	if line['attr'] == '{"id":"2833"}':
		stat_instance.hot_service_unlock_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.hot_service_unlock_khid_unidentification += 1
		else:
			stat_instance.hot_service_unlock_khid.append(line['khid'])

#分析进入开户页面
def analyse_hxaccount(line,stat_instance):
	stat_instance.hxaccount_pv += 1
	if line['khid'] == '' or line['khid'] == '-1':
		stat_instance.hxaccount_khid_unidentification += 1
	else:
		stat_instance.hxaccount_khid.append(line['khid'])
		
#分析进入推送
def analyse_recommend(line,stat_instance):
	if line['channel'] == '[e_recM]-recommend':		#早评
		stat_instance.recommend_enter_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_enter_khid_unidentification += 1
		else:
			stat_instance.recommend_enter_khid.append(line['khid'])
	elif line['channel'] == '[e_recn]-recommend_noon':		#午评
		stat_instance.recommend_noon_enter_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_noon_enter_khid_unidentification += 1
		else:
			stat_instance.recommend_noon_enter_khid.append(line['khid'])
	elif line['channel'] == '[e_rece]-recommend_noon':		#晚评
		stat_instance.recommend_eve_enter_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_eve_enter_khid_unidentification += 1
		else:
			stat_instance.recommend_eve_enter_khid.append(line['khid'])
			
#分析服务模块1_A点击
def analyse_service_1_areaA(line,stat_instance):
	if line['channel'] == '[e_recM]-recommend':		#早评
		stat_instance.recommend_service_1_areaA_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_service_1_areaA_khid_unidentification += 1
		else:
			stat_instance.recommend_service_1_areaA_khid.append(line['khid'])
	elif line['channel'] == '[e_recn]-recommend_noon':		#午评
		stat_instance.recommend_noon_service_1_areaA_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_noon_service_1_areaA_khid_unidentification += 1
		else:
			stat_instance.recommend_noon_service_1_areaA_khid.append(line['khid'])
	elif line['channel'] == '[e_rece]-recommend_noon':		#晚评
		stat_instance.recommend_eve_service_1_areaA_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_eve_service_1_areaA_khid_unidentification += 1
		else:
			stat_instance.recommend_eve_service_1_areaA_khid.append(line['khid'])
			
#分析服务模块1_B点击
def analyse_service_1_areaB(line,stat_instance):
	if line['channel'] == '[e_recM]-recommend':		#早评
		stat_instance.recommend_service_1_areaB_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_service_1_areaB_khid_unidentification += 1
		else:
			stat_instance.recommend_service_1_areaB_khid.append(line['khid'])
	elif line['channel'] == '[e_recn]-recommend_noon':		#午评
		stat_instance.recommend_noon_service_1_areaB_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_noon_service_1_areaB_khid_unidentification += 1
		else:
			stat_instance.recommend_noon_service_1_areaB_khid.append(line['khid'])
	elif line['channel'] == '[e_rece]-recommend_noon':		#晚评
		stat_instance.recommend_eve_service_1_areaB_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_eve_service_1_areaB_khid_unidentification += 1
		else:
			stat_instance.recommend_eve_service_1_areaB_khid.append(line['khid'])
			

#分析服务模块2_A点击
def analyse_service_2_areaA(line,stat_instance):
	if line['channel'] == '[e_recM]-recommend':		#早评
		stat_instance.recommend_service_2_areaA_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_service_2_areaA_khid_unidentification += 1
		else:
			stat_instance.recommend_service_2_areaA_khid.append(line['khid'])
	elif line['channel'] == '[e_recn]-recommend_noon':		#午评
		stat_instance.recommend_noon_service_2_areaA_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_noon_service_2_areaA_khid_unidentification += 1
		else:
			stat_instance.recommend_noon_service_2_areaA_khid.append(line['khid'])
	elif line['channel'] == '[e_rece]-recommend_noon':		#晚评
		stat_instance.recommend_eve_service_2_areaA_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_eve_service_2_areaA_khid_unidentification += 1
		else:
			stat_instance.recommend_eve_service_2_areaA_khid.append(line['khid'])
		
#分析服务模块2_B点击
def analyse_service_2_areaB(line,stat_instance):
	if line['channel'] == '[e_recM]-recommend':		#早评
		stat_instance.recommend_service_2_areaB_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_service_2_areaB_khid_unidentification += 1
		else:
			stat_instance.recommend_service_2_areaB_khid.append(line['khid'])
	elif line['channel'] == '[e_recn]-recommend_noon':		#午评
		stat_instance.recommend_noon_service_2_areaB_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_noon_service_2_areaB_khid_unidentification += 1
		else:
			stat_instance.recommend_noon_service_2_areaB_khid.append(line['khid'])
	elif line['channel'] == '[e_rece]-recommend_noon':		#晚评
		stat_instance.recommend_eve_service_2_areaB_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_eve_service_2_areaB_khid_unidentification += 1
		else:
			stat_instance.recommend_eve_service_2_areaB_khid.append(line['khid'])
			
		

#分析服务模块3_A点击
def analyse_service_3_areaA(line,stat_instance):
	if line['channel'] == '[e_recM]-recommend':		#早评
		stat_instance.recommend_service_3_areaA_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_service_3_areaA_khid_unidentification += 1
		else:
			stat_instance.recommend_service_3_areaA_khid.append(line['khid'])
	elif line['channel'] == '[e_recn]-recommend_noon':		#午评
		stat_instance.recommend_noon_service_3_areaA_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_noon_service_3_areaA_khid_unidentification += 1
		else:
			stat_instance.recommend_noon_service_3_areaA_khid.append(line['khid'])
	elif line['channel'] == '[e_rece]-recommend_noon':		#晚评
		stat_instance.recommend_eve_service_3_areaA_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_eve_service_3_areaA_khid_unidentification += 1
		else:
			stat_instance.recommend_eve_service_3_areaA_khid.append(line['khid'])
		
#分析服务模块3_B点击
def analyse_service_3_areaB(line,stat_instance):
	if line['channel'] == '[e_recM]-recommend':		#早评
		stat_instance.recommend_service_3_areaB_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_service_3_areaB_khid_unidentification += 1
		else:
			stat_instance.recommend_service_3_areaB_khid.append(line['khid'])
	elif line['channel'] == '[e_recn]-recommend_noon':		#午评
		stat_instance.recommend_noon_service_3_areaB_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_noon_service_3_areaB_khid_unidentification += 1
		else:
			stat_instance.recommend_noon_service_3_areaB_khid.append(line['khid'])
	elif line['channel'] == '[e_rece]-recommend_noon':		#晚评
		stat_instance.recommend_eve_service_3_areaB_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_eve_service_3_areaB_khid_unidentification += 1
		else:
			stat_instance.recommend_eve_service_3_areaB_khid.append(line['khid'])
			
