l = []
for i in range(7) :
    e = int(input())
    if e % 2 == 1 :
        l.append(e)
if l :
    print(sum(l))
    print(min(l))
else :
    print(-1)