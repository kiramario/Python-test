# -*- coding: utf-8 -*-


#���������ȵ�ҳ��
def analyse_hot_service(line,stat_instance):
	if line['attr'] == '{"id":"2833"}':
		stat_instance.hot_service_pv += 1
		if line['khid'] == '' or line['khid'] == '-1': 
			stat_instance.hot_service_khid_unidentification += 1
		else:
			stat_instance.hot_service_khid.append(line['khid'])

#������������ȵ�ҳ��
def analyse_hot_service_share(line,stat_instance):
	if line['attr'] == '{"id":"2833"}':
		stat_instance.hot_service_share_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.hot_service_share_khid_unidentification += 1
		else:
			stat_instance.hot_service_share_khid.append(line['khid'])
			
#���������ȵ�
def analyse_hot_service_unlock(line,stat_instance):
	if line['attr'] == '{"id":"2833"}':
		stat_instance.hot_service_unlock_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.hot_service_unlock_khid_unidentification += 1
		else:
			stat_instance.hot_service_unlock_khid.append(line['khid'])

#�������뿪��ҳ��
def analyse_hxaccount(line,stat_instance):
	stat_instance.hxaccount_pv += 1
	if line['khid'] == '' or line['khid'] == '-1':
		stat_instance.hxaccount_khid_unidentification += 1
	else:
		stat_instance.hxaccount_khid.append(line['khid'])
		
#������������
def analyse_recommend(line,stat_instance):
	if line['channel'] == '[e_recM]-recommend':		#����
		stat_instance.recommend_enter_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_enter_khid_unidentification += 1
		else:
			stat_instance.recommend_enter_khid.append(line['khid'])
	elif line['channel'] == '[e_recn]-recommend_noon':		#����
		stat_instance.recommend_noon_enter_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_noon_enter_khid_unidentification += 1
		else:
			stat_instance.recommend_noon_enter_khid.append(line['khid'])
	elif line['channel'] == '[e_rece]-recommend_noon':		#����
		stat_instance.recommend_eve_enter_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_eve_enter_khid_unidentification += 1
		else:
			stat_instance.recommend_eve_enter_khid.append(line['khid'])
			
#��������ģ��1_A���
def analyse_service_1_areaA(line,stat_instance):
	if line['channel'] == '[e_recM]-recommend':		#����
		stat_instance.recommend_service_1_areaA_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_service_1_areaA_khid_unidentification += 1
		else:
			stat_instance.recommend_service_1_areaA_khid.append(line['khid'])
	elif line['channel'] == '[e_recn]-recommend_noon':		#����
		stat_instance.recommend_noon_service_1_areaA_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_noon_service_1_areaA_khid_unidentification += 1
		else:
			stat_instance.recommend_noon_service_1_areaA_khid.append(line['khid'])
	elif line['channel'] == '[e_rece]-recommend_noon':		#����
		stat_instance.recommend_eve_service_1_areaA_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_eve_service_1_areaA_khid_unidentification += 1
		else:
			stat_instance.recommend_eve_service_1_areaA_khid.append(line['khid'])
			
#��������ģ��1_B���
def analyse_service_1_areaB(line,stat_instance):
	if line['channel'] == '[e_recM]-recommend':		#����
		stat_instance.recommend_service_1_areaB_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_service_1_areaB_khid_unidentification += 1
		else:
			stat_instance.recommend_service_1_areaB_khid.append(line['khid'])
	elif line['channel'] == '[e_recn]-recommend_noon':		#����
		stat_instance.recommend_noon_service_1_areaB_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_noon_service_1_areaB_khid_unidentification += 1
		else:
			stat_instance.recommend_noon_service_1_areaB_khid.append(line['khid'])
	elif line['channel'] == '[e_rece]-recommend_noon':		#����
		stat_instance.recommend_eve_service_1_areaB_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_eve_service_1_areaB_khid_unidentification += 1
		else:
			stat_instance.recommend_eve_service_1_areaB_khid.append(line['khid'])
			

#��������ģ��2_A���
def analyse_service_2_areaA(line,stat_instance):
	if line['channel'] == '[e_recM]-recommend':		#����
		stat_instance.recommend_service_2_areaA_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_service_2_areaA_khid_unidentification += 1
		else:
			stat_instance.recommend_service_2_areaA_khid.append(line['khid'])
	elif line['channel'] == '[e_recn]-recommend_noon':		#����
		stat_instance.recommend_noon_service_2_areaA_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_noon_service_2_areaA_khid_unidentification += 1
		else:
			stat_instance.recommend_noon_service_2_areaA_khid.append(line['khid'])
	elif line['channel'] == '[e_rece]-recommend_noon':		#����
		stat_instance.recommend_eve_service_2_areaA_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_eve_service_2_areaA_khid_unidentification += 1
		else:
			stat_instance.recommend_eve_service_2_areaA_khid.append(line['khid'])
		
#��������ģ��2_B���
def analyse_service_2_areaB(line,stat_instance):
	if line['channel'] == '[e_recM]-recommend':		#����
		stat_instance.recommend_service_2_areaB_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_service_2_areaB_khid_unidentification += 1
		else:
			stat_instance.recommend_service_2_areaB_khid.append(line['khid'])
	elif line['channel'] == '[e_recn]-recommend_noon':		#����
		stat_instance.recommend_noon_service_2_areaB_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_noon_service_2_areaB_khid_unidentification += 1
		else:
			stat_instance.recommend_noon_service_2_areaB_khid.append(line['khid'])
	elif line['channel'] == '[e_rece]-recommend_noon':		#����
		stat_instance.recommend_eve_service_2_areaB_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_eve_service_2_areaB_khid_unidentification += 1
		else:
			stat_instance.recommend_eve_service_2_areaB_khid.append(line['khid'])
			
		

#��������ģ��3_A���
def analyse_service_3_areaA(line,stat_instance):
	if line['channel'] == '[e_recM]-recommend':		#����
		stat_instance.recommend_service_3_areaA_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_service_3_areaA_khid_unidentification += 1
		else:
			stat_instance.recommend_service_3_areaA_khid.append(line['khid'])
	elif line['channel'] == '[e_recn]-recommend_noon':		#����
		stat_instance.recommend_noon_service_3_areaA_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_noon_service_3_areaA_khid_unidentification += 1
		else:
			stat_instance.recommend_noon_service_3_areaA_khid.append(line['khid'])
	elif line['channel'] == '[e_rece]-recommend_noon':		#����
		stat_instance.recommend_eve_service_3_areaA_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_eve_service_3_areaA_khid_unidentification += 1
		else:
			stat_instance.recommend_eve_service_3_areaA_khid.append(line['khid'])
		
#��������ģ��3_B���
def analyse_service_3_areaB(line,stat_instance):
	if line['channel'] == '[e_recM]-recommend':		#����
		stat_instance.recommend_service_3_areaB_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_service_3_areaB_khid_unidentification += 1
		else:
			stat_instance.recommend_service_3_areaB_khid.append(line['khid'])
	elif line['channel'] == '[e_recn]-recommend_noon':		#����
		stat_instance.recommend_noon_service_3_areaB_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_noon_service_3_areaB_khid_unidentification += 1
		else:
			stat_instance.recommend_noon_service_3_areaB_khid.append(line['khid'])
	elif line['channel'] == '[e_rece]-recommend_noon':		#����
		stat_instance.recommend_eve_service_3_areaB_pv += 1
		if line['khid'] == '' or line['khid'] == '-1':
			stat_instance.recommend_eve_service_3_areaB_khid_unidentification += 1
		else:
			stat_instance.recommend_eve_service_3_areaB_khid.append(line['khid'])
			
