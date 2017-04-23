#coding=utf-8
import fileinput, re

pattern = re.compile('From: (.*)<.*?>$')
for line in fileinput.input():
    m=pattern.match(line)
    if m: print m.group(1)  #获取给定子模式（组）的匹配项
    