n = int(input())
for i in range(n) :
    l = list(map(int, input().split()))
    cnt = 0
    
    temp_l = l[1:]
    avg = sum(temp_l)/l[0]
    for a in temp_l :
        if a > avg :
            cnt += 1
    print(f"{round(cnt/l[0]*100, 3):.3f}%")