A, B = map(int, input().split())
N = int(input())

l = set()
for i in range(N) :
    l.add(int(input()))

if A == B : 
    print(0)
    exit()

if B in l :
    print(1)
    exit()
else :
    temp = [abs(A-B)]
    for i in l :
        temp.append(abs(B-i))
    if temp.index(min(temp)) == 0 :
        print(abs(A-B))
    else :
        print(temp[temp.index(min(temp))] + 1)
