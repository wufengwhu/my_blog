import sys
if len(sys.argv) !=2
    print "Please supply a filename"
    raise SystemExit(1)

f = open(sys.argv[1])
lines = f.readlines()
f.close()
#将所有输入值从字符串转换为浮点数
fvalues = [float(line) for line in lines]

print "The minimum value is ", min(fvalues)
print "The maximum value is ", max(fvalues) 