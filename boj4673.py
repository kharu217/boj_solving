def self_num(n) :
    temp = n
    for i in str(n) :
        temp += int(i)
    return temp

l = set()
for i in range(1, 100001) :
    l.add(self_num(i))

self_n = [i for i in range(1, 10001)]
i = 9
for s in self_n :
    if s not in l :
        print(s)
    else :
        continue
