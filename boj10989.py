N = int(input())

N_d = dict()

for i in range(N) :
    temp = int(input())
    if temp not in N_d.keys() :
        N_d[temp] = 1
    else :
        N_d[temp] += 1

d1 = sorted(N_d.items())

for t in d1 :
    for _ in range(N_d[t]) :
        print(t)