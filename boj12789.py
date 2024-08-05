N = int(input())

right_N = [i for i in range(1, N + 1)]

N_l = list(map(int, input().split()))
area = []

cur_i = 1

while area or N_l :
    if N_l :
        if N_l[0] == cur_i :
            N_l.pop(0)
            cur_i += 1
        elif N_l[0] > cur_i :
            try :
                if area[0] == cur_i :
                    area.pop(0)
                    cur_i += 1
                    continue
                else :
                    area.insert(0, N_l.pop(0))
            except :
                area.insert(0, N_l.pop(0))
    else :
        if area[0] == cur_i :
            area.pop(0)
            cur_i += 1
        elif area[0] > cur_i :
            break

if area or N_l :
    print('Sad')
else :
    print('Nice')
