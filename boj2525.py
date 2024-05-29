N,M = map(int, input().split())
T = int(input())

N += T // 60
M += (T - (60 * (T // 60)))

if M >= 60 :
    N += 1
    M -= 60
    
if N >= 24 :
    N = 0

print(N, M)
