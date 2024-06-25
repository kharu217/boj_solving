import sys

N = int(sys.stdin.readline())

N_l = []

for i in range(N) :
    N_l.append(list(map(int, sys.stdin.readline().split())))

N_l.sort()
for t in N_l :
    print(t[0], t[1])
