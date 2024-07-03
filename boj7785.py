N = int(input())
l = dict()
s_l = []

for i in range(N) :
    temp = list(input().split())
    l[temp[0]] = temp[1]

for t in l.keys() :
    if l[t] == 'enter' :
        s_l.append(t)

for s in s_l :
    print(s)