N, M = map(int, input().split())
l = list(map(int, input().split()))
l.sort(reverse=True)

print(l[M - 1])
