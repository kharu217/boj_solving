n, d = map(int, input().split())

cnt = 0
for i in range(1, n + 1) :
    tmp = str(i)
    cnt += tmp.count(str(d))
print(cnt)