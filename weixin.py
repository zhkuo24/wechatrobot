# -*- coding: utf-8 -*-
import werobot
import time

robot = werobot.WeRoBot(token='Zhangkuo')
@robot.handler
def echo(message):
    return 'I love You cuicui!'

@robot.text
def echo(message):
    return message.content + '\n' + 'I Love You CuiCui' + "张阔\n" + time.strftime("%Y-%m-%d-%H:%M:%S %Z",time.localtime(time.time()))
@robot.filter("a")
def a():
    return "正文为 a "
robot.run()
