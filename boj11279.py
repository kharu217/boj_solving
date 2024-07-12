import heapq
from sys import stdin

input = stdin.readline

N = int(input())
l = []

for i in range(N) :
    cmd = -int(input())
    if cmd == 0 :
        try :
            print(-heapq.heappop(l))
        except :
            print(0)
    else :
        heapq.heappush(l, cmd)