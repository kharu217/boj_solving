N = int(input())
result = 0

for i in range(1, N + 1) :
    num = list(map(int, str(i)))
    s = sum(num) + i
    if s == N :
        print(i)
        break
    else :
        continue
else :
    print(0)