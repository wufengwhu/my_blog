principle = 1000
rate = 0.05
numyears = 5
year = 1
f = open("foo.txt")
fw = open("foo.txt", "w")
line = f.readline()
while line:
    print line
    line = f.readline()

while year <= numyears:
    principle  = principle * (1 + rate)
    print >> fw, "%3d %0.2f" % (year, principle)
    year +=1
f.close()
