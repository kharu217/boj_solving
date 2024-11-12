n = list(map(int, input().split()))
l = int(10e100)

cnt = 0
for i in range(min(n), l + 1) :
    for t in n :
        if i % t == 0 :
            cnt += 1
    if cnt >= 3 :
        print(i)
        break
    else :
        cnt = 0
