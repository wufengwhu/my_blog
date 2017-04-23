# coding=utf-8
s  = set([3,5,9,10])
print s
t = set("Hello")
print t
a = t | s #并集
b = t & s
c = t - s

t.add('X')
s.update([10,37,42]) #添加多项
t.remove('H')
d = t ^ s # 对称差集
print d