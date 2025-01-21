from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
l = deque()

for i in range(N) :
    cmd = input().replace('\n', '')
    if 'push_front' in cmd :
        l.append(int(cmd.split()[-1]))
    elif "push_back" in cmd :
        l.appendleft(int(cmd.split()[-1]))
    elif "pop_front" in cmd :
        if l :
          print(l.pop())
        else :
            print(-1)
    elif "pop_back" in cmd :
        if l :
          print(l.popleft())
        else :
            print(-1)
    elif cmd == "size" :
        print(len(l))
    elif cmd == "empty" :
        print(int(not bool(l)))
    elif "front" in cmd :
        if l :
          print(l[-1])
        else :
            print(-1)
    elif "back" in cmd :
        if l :
          print(l[0])
        else :
            print(-1)