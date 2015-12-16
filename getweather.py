# encoding: utf-8
__author__ = "zhangk"
"""
@version:0.1
@author: zhangk
@contact: zhangk1989@gmail.com
@file: getweather.py
"""
import requests
import json

class GetWeather():
	"""利用和风天气的api得到城市的天气信息"""
	def __init__(self, city):
		super(GetWeather, self).__init__()
		self.cityname = city
		self.key = 'b50ba365dd554fc887f14699a6e30584'
		self.url = "https://api.heweather.com/x3/weather"

	def getweatherinfo(self):

		weather_req = requests.get(self.url,params={'city':self.cityname,'key':self.key})
		weatherinfo_tmp =  weather_req.json()
		weather_basic = weatherinfo_tmp["HeWeather data service 3.0"][0]["basic"]
		weather_now = weatherinfo_tmp["HeWeather data service 3.0"][0]["now"]
		weather_aqi = weatherinfo_tmp["HeWeather data service 3.0"][0]["aqi"]
		weather_suggestion = weatherinfo_tmp["HeWeather data service 3.0"][0]["suggestion"]
		
		#weatherinfo = [('city','update','tmp','fl','hum','txt'),(weather_basic["city"])]
		weatherinfo = {
						'city':'',
						'update':'',
						'cond':'',
						'tmp':'',
						'fl':'',
						'hum':'',
						'sc':'',
						'aqi':'',
						'pm25':'',
						'pm10':'',
						'qlty':'',
						'comf':'',
						'drsg':'',
						'uv':''
		}
		weatherinfo['city'] = weather_basic['city']
		weatherinfo['update'] = weather_basic['update']['loc']
		weatherinfo['cond'] = weather_now['cond']['txt']
		weatherinfo['tmp'] = weather_now['tmp']
		weatherinfo['fl'] = weather_now['fl']
		weatherinfo['hum'] = weather_now['hum']
		weatherinfo['sc'] = weather_now['wind']['sc']
		weatherinfo['aqi'] =weather_aqi['city']['aqi']
		weatherinfo['pm25'] = weather_aqi['city']['pm25']
		weatherinfo['pm10'] = weather_aqi['city']['pm10']
		weatherinfo['qlty'] = weather_aqi['city']['qlty']
		weatherinfo['comf'] = weather_suggestion['comf']['txt']
		weatherinfo['drsg'] = weather_suggestion['drsg']['txt']
		weatherinfo['uv'] = weather_suggestion['uv']['txt']
		#weatherinfo_str1 = "城市："+ weatherinfo['city'] + '\n' + "更新时间：" + weatherinfo['update'] + '\n' + '\n'
		#weatherinfo_str2 = "天气：" + weatherinfo['cond'] + "     温度：" + weatherinfo['tmp'] + '°C' + '\n' + "湿度：" + weatherinfo['hum'] + '%' + "  风力等级" + weatherinfo['sc'] + '\n' + '\n'
		#weatherinfo_str3 = "空气质量指数：" + weatherinfo['aqi'] + '\n' + "PM2.5值：" + weatherinfo['pm25'] + '\n' + "PM10值： " + weatherinfo['pm10'] + '\n' + "空气质量类别：" + weatherinfo['qlty'] + '\n' + '\n'
		#weatherinfo_str4 = "穿衣指数：" + weatherinfo['drsg'] + '\n' + '\n' + "紫外线指数：" + weatherinfo['uv'] + '\n' + '\n'
		#weatherinfo_str = weatherinfo_str1 + weatherinfo_str2 + weatherinfo_str3 + weatherinfo_str4
		weatherinfo_str = '城市：%s\n更新时间：%s\n\n天气：%s     温度：%s°C\n湿度：%s  风力等级%s\n\n空气质量指数：%s\nPM2.5值：%s\nPM10值： %s\n空气质量类别：\
		%s\n\n穿衣指数：%s\n紫外线指数：%s\n'%(weatherinfo['city'],weatherinfo['update'],weatherinfo['cond'],weatherinfo['tmp'],weatherinfo['hum'],\
			weatherinfo['sc'],weatherinfo['aqi'],weatherinfo['pm25'],weatherinfo['pm10'],weatherinfo['qlty'],weatherinfo['drsg'],weatherinfo['uv'])
		return weatherinfo_str