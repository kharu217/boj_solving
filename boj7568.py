N = int(input())

l = []
rate_l = []

for i in range(N) :
    l.append(tuple(map(int, input().split())))

for T in l :
    rate_c = 0
    for F in l :
        if T[0] < F[0] and T[1] < F[1] :
            rate_c += 1
    rate_l.append(rate_c + 1)
    
for n in rate_l :
    print(n, end=' ')