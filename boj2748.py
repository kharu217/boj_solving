N = int(input())
l = [0, 1]
l.extend([0 for _ in range(N - 1)])

for i in range(2, N+1) :
    l[i] = l[i - 1] + l[i - 2]
print(l[-1])