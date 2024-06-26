N = []
max_l = []
w,h = 0, 0

for i in range(9) :
    N.append(list(map(int, input().split())))

for j in N :
    max_l.append(max(j))

for t in range(len(N)) :
    for s in range(len(N[t])) :
        if N[t][s] == max(max_l) :
            w = t
            h = s
            break
    
print(max(max_l))
print(w+1, h+1)