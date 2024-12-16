N, K = map(int, input().split())
l = [i for i in range(1, N + 1)]
q = []

while l :
    while K > len(l) :
        K -= len(l)
    q.append(l.pop(K-1))
    K += K - 1
print(q)

