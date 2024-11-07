N = int(input())
N_l = list(map(int, input().split()))
M = int(input())
M_l = list(map(int, input().split()))
M_d = {}
N_d = {}

for d in N_l :
    N_d[d] = 0

for i in M_l :
    M_d[i] = int(i in N_d.keys())

print(*M_d.values())
