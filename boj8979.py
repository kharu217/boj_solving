import sys

n, k = map(int, input().split())

l = []
for i in range(n) :
    temp = tuple(map(int, sys.stdin.readline().split()))
    l.append(temp[1:])
    if temp[0] == k :
        k = temp[1:]

l = list(set(l))

l.sort(key=lambda x : (x[0], x[1], x[2]), reverse=True)

print(l.index(k) + 1)
