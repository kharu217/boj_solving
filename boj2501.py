num, idx = map(int, input().split())

l = []
for i in range(1, num + 1) :
    if num % i == 0 :
        l.append(i)

if len(l) >= idx :
    print(l[idx - 1])
else :
    print(0)
