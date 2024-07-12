S = int(input())
temp_l = [0]
temp_l.extend(list(map(bool, (map(int, input().split())))))

N = int(input())
for t in range(N) :
    sx, switch = map(int, input().split())
    if sx == 1 :
        for d in range(len(temp_l)) :
            if d % switch == 0 :
                temp_l[d] = not temp_l[d]
    elif sx == 2 :
        pass
        cnt = 0
        for i in range(min(len(temp_l[:switch + 1]), len(temp_l[switch:]))) :
            if temp_l[switch + i] and temp_l[switch - i] :
                cnt = i
            else :
                for d in range(i + 1) :
                    temp_l[d + switch] = not temp_l[d + switch]

temp_l = list(map(int, temp_l))
for _ in range(1, len(temp_l)) :
    print(temp_l[_], end=' ')