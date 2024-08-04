N = int(input())

l = []

for _ in range(N) :
    l.append(list(map(int, input().split())))
    
for i in l :
    cnt = 0
    major = 0
    for m in i :
        if cnt == 0 :
            major = m
        if major == m :
            cnt += 1
        else :
            cnt -= 1
    if i.count(major) < round(len(i)/2 + 1e-10) :
        print('SYJKGW')
    else :
        print(major)
