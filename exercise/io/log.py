import logging
log=open('logfile.log', 'w')
print >> log, ('Download file from URL %s' % 'www.baidu.com')
logging.basicConfig(level=logging.INFO, filename='logfile.log')
