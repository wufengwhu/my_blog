#coding=utf-8
import string
import re
import itertools
from string import Template
a = "Hello Word"
b = a[4]
c = a[:5]
d = a[6:]
e = a[3:8]
g = a + " This is a test"
x = "37"
y = "42"
z = x + y
z = int(x) + int(y)
s = "The value of x is " + str(x)
s = "The value of x is " + str(x)
a1 = "Your name is {0} and your age is {age}"
name = "WuFeng"
r = "{0:>10}".format(name)
print r
print a1.format("Mike", age=40)
print '|', 'hej'.ljust(20),'|','hej'.rjust(20),'|','hej'.center(20),'|'#字符串对齐
print 'hej'.center(20, '*')
x = ' x  hej  '
print '|', x.lstrip(),'|','hej'.rstrip(),'|','hej'.strip(),'|'
#反转
revwords=x.join(x.split( )[::-1])#改变了原先的字符串中的空格
print revwords
revvwords = ''.join(reversed(re.split(r'(\s+)', x)))
print revvwords
# 模板
s = Template('$x, glorious $x!')
s.substitute(x='wufeng')
print s
#包含
# def containsAny(seq,aset):
#     for item in itertools.ifilter(aset.__contains__, seq):
#         return True
#     return False
def containsAny(seq, aset):
    for c in seq:
        if c in aset:return True
    return False





















