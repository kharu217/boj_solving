n = int(input())

l = []
d = dict()
for _ in range(n) :
    temp = list(map(int, input().split()))
    l.append(temp)
    d[temp[0]] = 0

l.sort(key=lambda x : x[2], reverse=True)
rate = 0
i = 0
while rate < 3:
    if d[l[i][0]] >= 2 :
        i += 1
        continue
    print(*l[i][:2])
    d[l[i][0]] += 1
    i += 1
    rate += 1