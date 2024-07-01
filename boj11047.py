import sys
input = sys.stdin.readline

N, M = map(int, input().split())

l = [int(input()) for i in range(N)]
l.reverse()
cnt = 0

for t in range(len(l)) :
    if l[t] > M :
        continue
    cnt += M // l[t]
    M %= l[t]

print(cnt)
