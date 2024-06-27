smap_l = [['' for _ in range(15)] for i in range(5)]


for s in range(5) :
    N = list(input())
    for i in range(len(N)) :
        smap_l[s][i] = N[i]

for w in range(15) :
    for h in range(5) :
        print(smap_l[h][w], end='')