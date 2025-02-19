s = input()
target = input()

if (len(s) == 1 and len(target) == 1) and s != target :
    print(-1)
    exit()

cnt = 0
for i in range(0, len(s)) :
    if s[i] != target[i] :
        cnt += 1
print(cnt)
