N = int(input())
l = []

for i in range(1, N + 1):
    if i == 1:
        l.append(1)
    elif i == 2:
        l.append(3)
    else:
        l.append((l[i-2] + 2 * l[i-3]) % 10007)
print(l[-1])