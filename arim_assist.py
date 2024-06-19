map_l = []

for i in range(10) :
    map_l.append(list(map(int, input().split())))

crt_w, crt_h = 1, 1

while True :

    if map_l[crt_w][crt_h] == 0 :
        map_l[crt_w][crt_h] = 9
    elif map_l[crt_w][crt_h] == 2 :
        map_l[crt_w][crt_h] = 9
        break

    if (map_l[crt_w+1][crt_h] == 1 and map_l[crt_w][crt_h+1] == 1) or (crt_w == 9 and crt_h == 9) :
        break
    
    if map_l[crt_w][crt_h+1] != 1 :
        crt_h += 1
        continue
    elif map_l[crt_w+1][crt_h] != 1 :
        crt_w += 1
        continue

for i in map_l :
    for t in i :
        print(t, end=' ')
     