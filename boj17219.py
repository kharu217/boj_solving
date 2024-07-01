import sys


N, M = map(int, sys.stdin.readline().rstrip().split())
l = dict()
l_s = []

for i in range(N) :
    a, b = sys.stdin.readline().rstrip().split()
    l[a] = b

for t in range(M) :
    l_s.append(sys.stdin.readline().rstrip())

for s in l_s :
    print(l[s])
