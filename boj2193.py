N = int(input())
l = [0] * 100001
l[0] = 1
l[1] = 1

if N > 2 :
    for i in range(2, N) :
        l[i] = l[i-1] + l[i-2]

print(l[N-1])
