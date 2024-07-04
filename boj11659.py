import sys
input = sys.stdin.readline

N, M = map(int, input().split())
n_l = list(map(int, input().split()))

for i in range(N) :
    res = 0
    A, B = map(int, input().split())
    print(sum(n_l[A - 1 : B]))
