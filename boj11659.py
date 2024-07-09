import sys
input = sys.stdin.readline

N, M = map(int, input().split())
n_l = list(map(int, input().split()))

s_l = [0]
res_ = 0
for i in n_l :
    res_ += i
    s_l.append(res_)

for _ in range(M) :
    A, B = map(int, input().split())
    print(s_l[B] - s_l[A - 1])
