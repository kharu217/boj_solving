T = int(input())

for i in range(T) :
    k = int(input())
    n = int(input())
    l = [x for x in range(1, n + 1)]
    for floor in range(k) :
        for s in range(1, n) :
            l[s] += l[s - 1]
    print(l[-1])
        