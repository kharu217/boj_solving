import sys

for i in range(3) :
    N = int(sys.stdin.readline().rstrip())
    num_l = []
    for t in range(N) :
        num_l.append(int(sys.stdin.readline().rstrip()))
    A = sum(num_l)
    if A == 0 :
        print(0)
    elif A > 0 :
        print('+')
    else :
        print('-')