from itertools import permutations
N, M = map(int, input().split())

l = list(range(1, N + 1))
per = permutations(l, M)

for i in per :
    print(*i)
