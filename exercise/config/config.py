#coding=utf-8
from ConfigParser import ConfigParser
CONFIGFILE="python.txt"

config=ConfigParser()
# 读取配置文件
config.read(CONFIGFILE)
#打印初始问候语句
# 要查看的区域是'message'
print config.get('messages', 'greeting')

# 打印配置文件中的结果信息
print config.get('messages', 'result_message'),  # 以逗号结束， 以在同一行显示
# getfloat()将config值转化为float类型:
radius=input(config.get('messages', 'question') + ' ')
print config.getfloat('numbers', 'pi')*radius**2
