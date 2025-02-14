a, b = map(int, input().split())

l = []
for i in range(1,b+1) :
    for n in range(0, i) :
        l.append(i)
print(sum(l[a-1:b]))
