N, M = map(int, input().split())

l = [i for i in range(1, N + 1)]

for _ in range(M) :
    s, w = map(int, input().split())
    temp = l[s-1]
    l[s-1] = l[w-1]
    l[w-1] = temp

for t in l :
    print(t, end=" ")
