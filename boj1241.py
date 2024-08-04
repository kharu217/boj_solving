import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
l = []
res = [0 for _ in range(N)]
for i in range(N) :
    l.append(int(input()))

matrix = [0 for _ in range(max(l) + 1)]

for num in l :
    matrix[num] += 1

for i in range(N) :
    k = 1
    while k*k <= (l[i]) :
        if l[i] % k == 0 :
            if k*k != l[i] :
                res[i] += matrix[k] + matrix[l[i]//k]
            else :
                res[i] += matrix[k]
        k += 1

for r in res :
    print(r - 1)
