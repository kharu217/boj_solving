import sys
from collections import deque

N = int(sys.stdin.readline())

queue1 = deque()

for i in range(N) :
    cmd = sys.stdin.readline().split()

    if 'push' in cmd :
        queue1.append(int(cmd[-1]))
    elif cmd == ['pop'] :
        try :
            print(queue1.pop())
        except :
            print(-1)
    elif cmd == ['size'] :
        print(len(queue1))
    elif cmd == ['empty'] :
        if len(queue1) == 0 :
            print(1)
        else :
            print(0)
    elif cmd == ['front'] :
        try :
            print(queue1[0])
        except :
            print(-1)
    elif cmd == ['back'] :
        try :
            print(queue1[-1])
        except :
            print(-1)