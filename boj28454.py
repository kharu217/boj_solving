cur_y, cur_m, cur_d = map(int, input().split('-'))

cnt = 0

n = int(input())

for i in range(n) :
    cou_y, cou_m, cou_d = map(int, input().split('-'))
    if cou_y > cur_y :
        cnt += 1
        continue
    elif cou_y == cur_y :
        if cou_m > cur_m :
            cnt += 1
            continue
        elif cou_m == cur_m :
            if cou_d > cur_d :
                cnt += 1
                continue
            elif cou_d == cur_d :
                cnt += 1
                continue
            else :
                continue
        else :
            continue
    else :
        continue

        
print(cnt)