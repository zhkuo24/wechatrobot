# -*- coding: utf-8 -*-
import werobot
import time
import pytz
import datetime

from getweather import GetWeather
from tuling import TuLing

from werobot.client import Client
robot = werobot.WeRoBot(token='Zhangkuo')
#@robot.handler
#def echo(message):
#    return 'I love You cuicui!'

#@robot.text
#def echo(message):
#    return message.content + '\n' + 'I Love You CuiCui' + "张阔\n" + time.strftime("%Y-%m-%d-%H:%M:%S %Z",time.localtime(time.time()))

"""
@robot.text
def echo(message):
	#获取时间信息
	tz = pytz.timezone('Asia/Shanghai')
	time_current = datetime.datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
	return message.content + '\n' + 'I Love You  来自WALL-E\n' + 'Time: ' + time_current
"""

"""
@robot.text
def echo_weather(message):	
	weather1 = GetWeather('wuhan').getweatherinfo()
	weather2 = GetWeather('shijiazhuang').getweatherinfo()
	return weather1 + weather2 + 'Time: ' + time_current
"""
#获取时间信息
tz = pytz.timezone('Asia/Shanghai')
time_current = datetime.datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')

#天气信息
@robot.filter("石家庄")
def echo_weather(message):
	weather = GetWeather(message.content).getweatherinfo()
	return weather + '\nTime: ' + time_current
@robot.filter("武汉")
def echo_weather(message):
	weather = GetWeather(message.content).getweatherinfo()
	return weather + '\nTime: ' + time_current

#小黄鸡
@robot.text
def robot_chat(message):
	robot_res = TuLing(message.content).robot_response()
	return robot_res


robot.run()
