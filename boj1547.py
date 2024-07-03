N = int(input())
cup = [1, 0, 0]

for i in range(N) :
    W, H = map(int, input().split())
    temp = cup[W - 1]
    cup[W - 1] = cup[H - 1]
    cup[H - 1] = temp

print(cup.index(1) + 1)
