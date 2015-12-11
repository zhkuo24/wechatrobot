# -*- coding: utf-8 -*-
import werobot
import time
import pytz
import datetime

robot = werobot.WeRoBot(token='Zhangkuo')
#@robot.handler
#def echo(message):
#    return 'I love You cuicui!'

#@robot.text
#def echo(message):
#    return message.content + '\n' + 'I Love You CuiCui' + "张阔\n" + time.strftime("%Y-%m-%d-%H:%M:%S %Z",time.localtime(time.time()))


@robot.text
def echo(message):
	#获取时间信息
	tz = pytz.timezone('Asia/Shanghai')
	time_current = datetime.datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
	return message.content + '\n' + 'I Love You  来自WALL-E\n' + 'Time: ' + time_current

robot.run()
