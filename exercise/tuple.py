#coding=utf-8
stock = ('GOOG', 100, 490.10)
address = ('www.python.org', 80)
person = ('first_name', 'last_name', 'phone')
a = ()
b = ('item',) #1-元组 （注意随后的逗号）
#解包
host, port = address
print host
print port
