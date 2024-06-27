paper = [[1 for _ in range(100)] for i in range(100)]

N = int(input())
result = 0

for t in range(N) :
    w, h = map(int, input().split())
    for a in range(h) :
        paper[a][w] = 1

for s in paper :
    result += sum(s)

print(result)