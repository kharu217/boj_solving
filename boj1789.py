N = int(input())
cnt = 0
i = 1

while N >= 0 :
    N -= i
    i += 1
    cnt += 1

print(cnt - 1)
