# -*- coding: utf-8 -*-

import werobot


robot = werobot.WeRoBot(token='Zhangkuo')
@robot.handler
def echo(message):
    return 'I love You cuicui!'

@robot.text
def echo(message):
    return message.content + 'I Love You CUICUI' + "张阔"
robot.run()
