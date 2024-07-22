N = int(input())

origin_l = [[0 for s in range(100)] for t in range(100)]
l = []

for i in range(N) :
    l.append(list(map(int, input().split())))

for p in l :
    for p2 in range(p[1], p[1] + 10) :
        for p3 in range(p[0], p[0] + 10) :
            origin_l[p2][p3] = 1
cnt = 0
for f in origin_l :
    for f2 in f :
        if f2 == 1 :
            cnt += 1
            
print(cnt)