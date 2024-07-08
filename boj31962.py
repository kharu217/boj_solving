N, M = map(int, input().split())
l = []

cor_l = []

for i in range(N) :
    l.append(tuple(map(int, input().split())))

for t in range(len(l)) :
    if sum(l[t]) <= M :
        cor_l.append(l[t][0])

if len(cor_l) == 0 :
    print(-1)
    exit()

print(max(cor_l))
