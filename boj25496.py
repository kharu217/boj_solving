P, N = map(int, input().split())
l = list(map(int, input().split()))
l.sort()

cnt = 0
try :
    while P < 200 :
        P += l.pop(0)
        cnt += 1
except :
    print(cnt)
    exit()
print(cnt)