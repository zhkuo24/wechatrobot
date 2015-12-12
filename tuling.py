# encoding: utf-8
__author__ = "zhangk"
"""
@version:0.1
@author: zhangk
@contact: zhangk1989@gmail.com
@file: tuling.py
"""
import requests
import json

class TuLing():
	"""机器人自动对话"""
	def __init__(self,request_text):
		super(TuLing, self).__init__()
		#self.key = '9ad9b977-6c3d-4d83-9c07-43d978a9614a'
		self.txet = request_text
		self.url = "http://sandbox.api.simsimi.com/request.p?key=9ad9b977-6c3d-4d83-9c07-43d978a9614a&lc=ch&ft=1.0&text="+self.txet
		

	def robot_response(self):

		robot_req = requests.get(self.url)
		robot_req_tmp =  robot_req.json()
		
		return robot_req_tmp['response']