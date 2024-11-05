N = int(input())
i = 2

l = []

if N == 1 :
    exit()
else :
    while N != 1 :
        if N%i == 0 :
            N /= i
            l.append(i)
            continue
        else :
            i += 1

for list_ in l :
    print(list_)
