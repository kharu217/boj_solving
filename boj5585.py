N = 1000 - int(input())
n_l = [500, 100, 50, 10, 5, 1]

cnt = 0

for i in n_l :
    while N >= i :
        N -= i
        cnt += 1

print(cnt)

