N, M = map(int, input().split())
l = [i for i in range(1, N+1)]

i = M-1
temp_l = []
while l != [] :
    if len(l) != 1 :
        if i > len(l) :
            temp = l.index(l[i//len(l)])+M-1
        else :
            temp = l.index(l[i-len(l)])+M-1

        if i > len(l) - 1 :
            temp_l.append(l.pop(i//len(l)))
        else :
            temp_l.append(l.pop(i))
        if temp > len(l) :
            i = temp - len(l)
        else :
            i = temp
    else :
        temp_l.append(l[0])
        l.pop(0)
print(f'<{temp_l}>')