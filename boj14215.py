l = list(map(int, input().split()))
l.sort()
if l[0] + l[1] > l[2] :
    print(sum(l))
else :
    print((l[0] + l[1]) * 2 - 1)
