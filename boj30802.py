import sys

N_m = int(sys.stdin.readline())

T_l = list(map(int, sys.stdin.readline().split()))

P_t, P_p = map(int, sys.stdin.readline().split())

T_sum = 0
for i in T_l :
    T_sum += i // P_t
    if i % P_t :
        T_sum += 1

print(T_sum)
print(N_m//P_p, N_m%P_p)