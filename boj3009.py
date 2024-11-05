l1 = []
l2 = []
last_pos = []
for i in range(3) :
    temp = list(map(int, input().split()))
    if i == 0 :
        l1.append(temp)
        temp_y = temp[0]
    else :
        if temp[0] == temp_y :
            l1.append(temp)
        else :
            l2.append(temp)
if len(l1) > len(l2) :
    last_pos.append(l2[0][0])
    last_pos.append(max((l1[0][0], l1[0][1])))
else :
    last_pos.append(l1[0][0])
