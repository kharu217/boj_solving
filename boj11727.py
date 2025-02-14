N = int(input())
l = [0] * 100001

for i in range(1, N + 1):
    if i == 1:
        l[i] = 1
    elif i == 2:
        l[i] = 3
    else:
        l[i] = (l[i-2] * 2+ l[i-1])
print(l[N] % 10007)