#coding=utf-8
#with语句 正确的管理各种系统资源（文件，锁定和连接）
#with语句只对支持上下文管理协议的对象有效
import threading
with open("foo.txt", "w") as f:
    f.write("Debugging\n")
    f.write("Done\n")

lock = threading.Lock()
with lock:
