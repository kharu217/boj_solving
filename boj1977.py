m = int(input())
n = int(input())

cnt = 0
min_ = 1e10

for i in range(m, n + 1) :
    if (i**0.5)%1 != 0.0 :
        continue
    else :
        cnt += i
        if i < min_ :
            min_ = i
if cnt == 0 :
    print(-1)
    exit()

print(cnt)
print(min_)    
