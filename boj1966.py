X = int(input())

for i in range(X) :
    cnt = 1
    N, M = map(int, input().split())
    l = list(map(int, input().split()))
    while True :
        target_l = l[M]
        
        if len(l) == 0 :
            break
        
        if l[0] == max(l) :
            if M == 0 :
                print(cnt)
                break
            else :
                l.pop(0)
                M -= 1
                cnt += 1
        else :
            l.append(l.pop(0))
            M -= 1
        if M < 0 :
            M += len(l)
                