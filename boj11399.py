N = int(input())
l = list(map(int, input().split()))
l.sort()
result = 0

for i in range(len(l)) :
    result += sum(l[:i + 1])

print(result)