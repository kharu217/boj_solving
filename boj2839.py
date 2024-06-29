N = int(input())

cnt = 0

while N >= 3 :
    if N % 5 == 0 :
        break
    N -= 3
    cnt += 1

while N >= 5 :
    N -= 5
    cnt += 1

if N == 0 :
    print(cnt)
else :
    print(-1)