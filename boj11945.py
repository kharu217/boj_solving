N, M = map(int, input().split())

l = []

for i in range(N) :
    temp = list(input())
    temp.reverse()
    l.append(temp)

for t in l :
    print(''.join(t))
