N, M = map(int, input().split())
cnt = 0

while 1 :
    if N >= 2 and M >= 1 :
        cnt += 1
        N -= 2
        M -= 1
    
    if N < 2 or M < 1 :
        break

print(cnt)