# -*- coding: utf-8 -*-
# 反复地以需要时间间隔执行某个命令

import os
import sys
import time


def main(cmd, inc=5):
    while True:
        os.system(cmd)
        time.sleep(inc)


if __name__ == '__main__':
    numargs = len(sys.argv) - 1
    if numargs < 1 or numargs > 2:
        print("usage: " + sys.argv[0] + " command [seconds_delay]")
        sys.exit(1)
    cmd = sys.argv[1]
    if numargs < 3:
        main(cmd)
    else:
        inc = int(sys.argv[2])
        main(cmd, inc)
