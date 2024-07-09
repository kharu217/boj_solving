N = int(input())
l = []

col = 0
row = 0

for _ in range(N) :
    l.append(list(input()))

t_cnt = 0
c_cnt = 0

for t in range(N) :
    for s in range(N) :
        if l[t][s] == '.' :
            c_cnt += 1
        else :
            if c_cnt >= 2 :
                col += 1
            c_cnt = 0
    if c_cnt >= 2 :
        col += 1
    c_cnt = 0

for t in range(N) :
    for s in range(N) :
        if l[s][t] == '.' :
            t_cnt += 1
        else :
            if t_cnt >= 2 :
                row += 1
            t_cnt = 0
    if t_cnt >= 2 :
        row += 1
    t_cnt = 0

print(col, row)