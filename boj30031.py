N = int(input())

s_l = {136 : 1000,
       142 : 5000,
       148 : 10000,
       154 : 50000}

l = []
result = 0

for i in range(N) :
    l.append(list(map(int, input().split()))[0])

for t in l :
    result += s_l[t]

print(result)