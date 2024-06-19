N = int(input())

for i in range(N) :
    sum = 0
    f, s = map(int, input().split())
    if f == 0 :
        pass
    elif f <= 1 :
        sum += 500
    elif f <= 3 :
        sum += 300
    elif f <= 6 :
        sum += 200
    elif f <= 10 :
        sum += 50
    elif f <= 15 :
        sum += 30
    elif f <= 21 :
        sum += 10
    
    if s == 0 :
        pass
    elif s <= 1 :
        sum += 512
    elif s <= 3 :
        sum += 256
    elif s <= 7 :
        sum += 128
    elif s <= 15 :
        sum += 64
    elif s <= 31 :
        sum += 32
    print(sum * 10000)