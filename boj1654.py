X = int(input())

for i in range(X) :
    cnt = 1
    N, M = map(int, input().split())
    l = list(map(int, input().split()))
    for t in range(len(l)) :
        if l[0] == max(l) :
            if t == M :
                print(cnt)
                break
            else :
                cnt += 1
                l.pop(0)
                M -= 1
        else :
            if t == M :
                l.append(l.pop(0))
                M = len(l)
            else :
                l.append(l.pop(0))