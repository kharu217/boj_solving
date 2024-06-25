import sys

M = int(sys.stdin.readline())
M_l = []

for i in range(M) :
    M_l.append(int(sys.stdin.readline()))

M_l.sort()
for t in M_l :
    print(t)
