#coding=utf-8
#tail一个文件（tail -f）
import time
def tail(f):
    f.seek(0, 2)   #移动到EOF
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line
def grep(line, searchtext):
    for line in lines:
        if searchtext in line:yield line
s = ["Hello WuFeng", "shang yu"]
stock = {
    "name" : "GOOG",
    "shares": 100,
    "price":490.10
}
it = s.__iter__()
while 1:
    try:
        i = it.next()
        print i
    except StopIteration:
        break
for i,x in enumerate(s):
    print i,x
for x,y in zip(s, stock):
    print x, y
#for-else
for line in open("foo.txt"):
    stripped = line.strip()
    if not stripped:
        break
    # 处理读出的行
 # else:
 #    raise RuntimeError("Missing section separator")
def countdown(n):
    print("Counting down from %d " % n)
    try:
        while n >0:
            yield n
            n -=1
    except GeneratorExit:
        print("Only made it to %d" %n)
f = open("generator_file.py")
lines = (t.strip() for t in f)   # 读取行，并删除前后空白
comments = (t for t in lines if t[0] == '#')  # 所有注释
for c in comments:
    print c