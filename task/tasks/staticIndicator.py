# -*- coding: utf-8 -*-

# ͳ��ָ��
class StatIndication(object):
	def __init__(self):
		#�����ȵ�ҳ��
		self.hot_service_pv = 0
		self.hot_service_uv = 0
		self.hot_service_khid = []
		self.hot_service_khid_unidentification = 0
		
		#�ȵ�ҳ��������
		self.hot_service_unlock_pv = 0
		self.hot_service_unlock_uv = 0
		self.hot_service_unlock_khid = []
		self.hot_service_unlock_khid_unidentification = 0
		
		#�����ȵ����ҳ��
		self.hot_service_share_pv = 0
		self.hot_service_share_uv = 0
		self.hot_service_share_khid = []
		self.hot_service_share_khid_unidentification = 0
		
		#���뿪��ҳ��
		self.hxaccount_pv = 0
		self.hxaccount_uv = 0
		self.hxaccount_khid = []
		self.hxaccount_khid_unidentification = 0

		#��������Ѷ�¼�
			#����
		self.recommend_enter_pv = 0
		self.recommend_enter_uv = 0
		self.recommend_enter_khid = []
		self.recommend_enter_khid_unidentification = 0
		
			#����
		self.recommend_noon_enter_pv = 0
		self.recommend_noon_enter_uv = 0
		self.recommend_noon_enter_khid = []
		self.recommend_noon_enter_khid_unidentification = 0
		
			#����
		self.recommend_eve_enter_pv = 0
		self.recommend_eve_enter_uv = 0
		self.recommend_eve_enter_khid = []
		self.recommend_eve_enter_khid_unidentification = 0
		
		#����ģ��1_A���-����
		self.recommend_service_1_areaA_pv = 0
		self.recommend_service_1_areaA_uv = 0
		self.recommend_service_1_areaA_khid = []
		self.recommend_service_1_areaA_khid_unidentification = 0
		
		#����ģ��1_A���-����
		self.recommend_noon_service_1_areaA_pv = 0
		self.recommend_noon_service_1_areaA_uv = 0
		self.recommend_noon_service_1_areaA_khid = []
		self.recommend_noon_service_1_areaA_khid_unidentification = 0
		
		#����ģ��1_A���-����
		self.recommend_eve_service_1_areaA_pv = 0
		self.recommend_eve_service_1_areaA_uv = 0
		self.recommend_eve_service_1_areaA_khid = []
		self.recommend_eve_service_1_areaA_khid_unidentification = 0
		
		#����ģ��1_B���-����
		self.recommend_service_1_areaB_pv = 0
		self.recommend_service_1_areaB_uv = 0
		self.recommend_service_1_areaB_khid = []
		self.recommend_service_1_areaB_khid_unidentification = 0
		
		#����ģ��1_B���-����
		self.recommend_noon_service_1_areaB_pv = 0
		self.recommend_noon_service_1_areaB_uv = 0
		self.recommend_noon_service_1_areaB_khid = []
		self.recommend_noon_service_1_areaB_khid_unidentification = 0
		
		#����ģ��1_B���-����
		self.recommend_eve_service_1_areaB_pv = 0
		self.recommend_eve_service_1_areaB_uv = 0
		self.recommend_eve_service_1_areaB_khid = []
		self.recommend_eve_service_1_areaB_khid_unidentification = 0
		
		#����ģ��2_A���-����
		self.recommend_service_2_areaA_pv = 0
		self.recommend_service_2_areaA_uv = 0
		self.recommend_service_2_areaA_khid = []
		self.recommend_service_2_areaA_khid_unidentification = 0
		
		#����ģ��2_A���-����
		self.recommend_noon_service_2_areaA_pv = 0
		self.recommend_noon_service_2_areaA_uv = 0
		self.recommend_noon_service_2_areaA_khid = []
		self.recommend_noon_service_2_areaA_khid_unidentification = 0
		
		#����ģ��2_A���-����
		self.recommend_eve_service_2_areaA_pv = 0
		self.recommend_eve_service_2_areaA_uv = 0
		self.recommend_eve_service_2_areaA_khid = []
		self.recommend_eve_service_2_areaA_khid_unidentification = 0
		
		#����ģ��2_B���-����
		self.recommend_service_2_areaB_pv = 0
		self.recommend_service_2_areaB_uv = 0
		self.recommend_service_2_areaB_khid = []
		self.recommend_service_2_areaB_khid_unidentification = 0
		
		#����ģ��2_B���-����
		self.recommend_noon_service_2_areaB_pv = 0
		self.recommend_noon_service_2_areaB_uv = 0
		self.recommend_noon_service_2_areaB_khid = []
		self.recommend_noon_service_2_areaB_khid_unidentification = 0
		
		#����ģ��2_B���-����
		self.recommend_eve_service_2_areaB_pv = 0
		self.recommend_eve_service_2_areaB_uv = 0
		self.recommend_eve_service_2_areaB_khid = []
		self.recommend_eve_service_2_areaB_khid_unidentification = 0
		
		
		
		#����ģ��3_A���-����
		self.recommend_service_3_areaA_pv = 0
		self.recommend_service_3_areaA_uv = 0
		self.recommend_service_3_areaA_khid = []
		self.recommend_service_3_areaA_khid_unidentification = 0
		
		#����ģ��3_A���-����
		self.recommend_noon_service_3_areaA_pv = 0
		self.recommend_noon_service_3_areaA_uv = 0
		self.recommend_noon_service_3_areaA_khid = []
		self.recommend_noon_service_3_areaA_khid_unidentification = 0
		
		#����ģ��3_A���-����
		self.recommend_eve_service_3_areaA_pv = 0
		self.recommend_eve_service_3_areaA_uv = 0
		self.recommend_eve_service_3_areaA_khid = []
		self.recommend_eve_service_3_areaA_khid_unidentification = 0
		
		#����ģ��3_B���-����
		self.recommend_service_3_areaB_pv = 0
		self.recommend_service_3_areaB_uv = 0
		self.recommend_service_3_areaB_khid = []
		self.recommend_service_3_areaB_khid_unidentification = 0
		
		#����ģ��3_B���-����
		self.recommend_noon_service_3_areaB_pv = 0
		self.recommend_noon_service_3_areaB_uv = 0
		self.recommend_noon_service_3_areaB_khid = []
		self.recommend_noon_service_3_areaB_khid_unidentification = 0
		
		#����ģ��3_B���-����
		self.recommend_eve_service_3_areaB_pv = 0
		self.recommend_eve_service_3_areaB_uv = 0
		self.recommend_eve_service_3_areaB_khid = []
		self.recommend_eve_service_3_areaB_khid_unidentification = 0
