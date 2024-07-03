set_l = ['0','1','2','3','4','5','6','7','8','6']
N = list(input())

cnt = 1

for i in N :
    t = i

    if t == '6' or t == '9' :
        if '6' not in set_l:
            set_l = ['0','1','2','3','4','5','6','7','8','6']
            set_l.remove('6')
            cnt += 1
            continue
        else :
            set_l.remove('6')
            continue
    if t not in set_l :
        set_l = ['0','1','2','3','4','5','6','7','8','6']
        set_l.remove(t)
        cnt += 1
        continue
    else :
        set_l.remove(t)
        continue

print(cnt)