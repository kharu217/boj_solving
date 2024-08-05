N = int(input())
l = list(set(map(int, input().split())))
l.sort()

print(*l)
