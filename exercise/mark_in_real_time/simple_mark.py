import sys, re
from listing1 import *

print '<html><head><title>...</title><body>'

title=True
for block in blocks(sys.stdin):
    block=re.sub(r'\*(.+?)\*',r'<em>\1</em>', block)  # not greedy 的重复运算符
    if title:
        print '<h1>'
        print block
        print '</h1>'
        title=False
    else:
        print '<p>'
        print blockb
        print '</p>'
        print '</body></head></html>'     
