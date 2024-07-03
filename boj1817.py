N, M = map(int, input().split())
if N == 0 :
    print(0)
    exit()
else :
    l = list(map(int, input().split()))
box = []
temp = []

for i in range(len(l)) :
    t = l[i]
    if sum(temp) + l[i] <= M :
        temp.append(l[i])
    else :
        box.append(temp)
        temp = []
        temp.append(l[i])



print(len(box) + 1)
