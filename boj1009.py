import sys

N = int(sys.stdin.readline().rstrip())

for i in range(N) :
    A, B = map(int, sys.stdin.readline().rstrip().split())
    res = A
    for _ in range(2, B + 1) :
        res *= A
        res %= 10
    if res == 0 :
        print(10)
    else :
        print(res)