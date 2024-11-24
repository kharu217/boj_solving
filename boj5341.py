while True :
    n = int(input())
    if n == 0 :
        break
    cnt = 0
    for i in range(n) :
        cnt += n - i
    print(cnt)
