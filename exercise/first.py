import math
import sys
import urllib2
print 1+1
html = urllib2.urlopen("http://www.baidu.com")
print html.readline()
for x in xrange(1,10):
    print x

sys.path.append('/Users/fengwu/Documents/Python')