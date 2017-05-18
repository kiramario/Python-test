# -*- coding: utf-8 -*-

# 统计指标
class StatIndication(object):
	def __init__(self):
		#进入热点页面
		self.hot_service_pv = 0
		self.hot_service_uv = 0
		self.hot_service_khid = []
		self.hot_service_khid_unidentification = 0
		
		#热点页面点击解锁
		self.hot_service_unlock_pv = 0
		self.hot_service_unlock_uv = 0
		self.hot_service_unlock_khid = []
		self.hot_service_unlock_khid_unidentification = 0
		
		#进入热点分享页面
		self.hot_service_share_pv = 0
		self.hot_service_share_uv = 0
		self.hot_service_share_khid = []
		self.hot_service_share_khid_unidentification = 0
		
		#进入开户页面
		self.hxaccount_pv = 0
		self.hxaccount_uv = 0
		self.hxaccount_khid = []
		self.hxaccount_khid_unidentification = 0

		#早中晚资讯事件
			#早评
		self.recommend_enter_pv = 0
		self.recommend_enter_uv = 0
		self.recommend_enter_khid = []
		self.recommend_enter_khid_unidentification = 0
		
			#午评
		self.recommend_noon_enter_pv = 0
		self.recommend_noon_enter_uv = 0
		self.recommend_noon_enter_khid = []
		self.recommend_noon_enter_khid_unidentification = 0
		
			#晚评
		self.recommend_eve_enter_pv = 0
		self.recommend_eve_enter_uv = 0
		self.recommend_eve_enter_khid = []
		self.recommend_eve_enter_khid_unidentification = 0
		
		#服务模块1_A点击-早评
		self.recommend_service_1_areaA_pv = 0
		self.recommend_service_1_areaA_uv = 0
		self.recommend_service_1_areaA_khid = []
		self.recommend_service_1_areaA_khid_unidentification = 0
		
		#服务模块1_A点击-午评
		self.recommend_noon_service_1_areaA_pv = 0
		self.recommend_noon_service_1_areaA_uv = 0
		self.recommend_noon_service_1_areaA_khid = []
		self.recommend_noon_service_1_areaA_khid_unidentification = 0
		
		#服务模块1_A点击-晚评
		self.recommend_eve_service_1_areaA_pv = 0
		self.recommend_eve_service_1_areaA_uv = 0
		self.recommend_eve_service_1_areaA_khid = []
		self.recommend_eve_service_1_areaA_khid_unidentification = 0
		
		#服务模块1_B点击-早评
		self.recommend_service_1_areaB_pv = 0
		self.recommend_service_1_areaB_uv = 0
		self.recommend_service_1_areaB_khid = []
		self.recommend_service_1_areaB_khid_unidentification = 0
		
		#服务模块1_B点击-午评
		self.recommend_noon_service_1_areaB_pv = 0
		self.recommend_noon_service_1_areaB_uv = 0
		self.recommend_noon_service_1_areaB_khid = []
		self.recommend_noon_service_1_areaB_khid_unidentification = 0
		
		#服务模块1_B点击-晚评
		self.recommend_eve_service_1_areaB_pv = 0
		self.recommend_eve_service_1_areaB_uv = 0
		self.recommend_eve_service_1_areaB_khid = []
		self.recommend_eve_service_1_areaB_khid_unidentification = 0
		
		#服务模块2_A点击-早评
		self.recommend_service_2_areaA_pv = 0
		self.recommend_service_2_areaA_uv = 0
		self.recommend_service_2_areaA_khid = []
		self.recommend_service_2_areaA_khid_unidentification = 0
		
		#服务模块2_A点击-午评
		self.recommend_noon_service_2_areaA_pv = 0
		self.recommend_noon_service_2_areaA_uv = 0
		self.recommend_noon_service_2_areaA_khid = []
		self.recommend_noon_service_2_areaA_khid_unidentification = 0
		
		#服务模块2_A点击-晚评
		self.recommend_eve_service_2_areaA_pv = 0
		self.recommend_eve_service_2_areaA_uv = 0
		self.recommend_eve_service_2_areaA_khid = []
		self.recommend_eve_service_2_areaA_khid_unidentification = 0
		
		#服务模块2_B点击-早评
		self.recommend_service_2_areaB_pv = 0
		self.recommend_service_2_areaB_uv = 0
		self.recommend_service_2_areaB_khid = []
		self.recommend_service_2_areaB_khid_unidentification = 0
		
		#服务模块2_B点击-午评
		self.recommend_noon_service_2_areaB_pv = 0
		self.recommend_noon_service_2_areaB_uv = 0
		self.recommend_noon_service_2_areaB_khid = []
		self.recommend_noon_service_2_areaB_khid_unidentification = 0
		
		#服务模块2_B点击-晚评
		self.recommend_eve_service_2_areaB_pv = 0
		self.recommend_eve_service_2_areaB_uv = 0
		self.recommend_eve_service_2_areaB_khid = []
		self.recommend_eve_service_2_areaB_khid_unidentification = 0
		
		
		
		#服务模块3_A点击-早评
		self.recommend_service_3_areaA_pv = 0
		self.recommend_service_3_areaA_uv = 0
		self.recommend_service_3_areaA_khid = []
		self.recommend_service_3_areaA_khid_unidentification = 0
		
		#服务模块3_A点击-午评
		self.recommend_noon_service_3_areaA_pv = 0
		self.recommend_noon_service_3_areaA_uv = 0
		self.recommend_noon_service_3_areaA_khid = []
		self.recommend_noon_service_3_areaA_khid_unidentification = 0
		
		#服务模块3_A点击-晚评
		self.recommend_eve_service_3_areaA_pv = 0
		self.recommend_eve_service_3_areaA_uv = 0
		self.recommend_eve_service_3_areaA_khid = []
		self.recommend_eve_service_3_areaA_khid_unidentification = 0
		
		#服务模块3_B点击-早评
		self.recommend_service_3_areaB_pv = 0
		self.recommend_service_3_areaB_uv = 0
		self.recommend_service_3_areaB_khid = []
		self.recommend_service_3_areaB_khid_unidentification = 0
		
		#服务模块3_B点击-午评
		self.recommend_noon_service_3_areaB_pv = 0
		self.recommend_noon_service_3_areaB_uv = 0
		self.recommend_noon_service_3_areaB_khid = []
		self.recommend_noon_service_3_areaB_khid_unidentification = 0
		
		#服务模块3_B点击-晚评
		self.recommend_eve_service_3_areaB_pv = 0
		self.recommend_eve_service_3_areaB_uv = 0
		self.recommend_eve_service_3_areaB_khid = []
		self.recommend_eve_service_3_areaB_khid_unidentification = 0
