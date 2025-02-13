S = list(input())[::-1]
S_target = list(input())[::-1]

cnt = 0
if sorted(S) != sorted(S_target) :
    print(-1)
    exit()
for i in range(0, len(S)) :
    if S[i] != S_target[i] :
        S.pop(0)
        cnt += 1
    else :
        continue
print(cnt) 
