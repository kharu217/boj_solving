N = int(input())
cnt = 0

while N >= 2 :
    if N % 5 == 0 :
        break
    N -= 2
    cnt += 1


while N >= 5 :
    N -= 5
    cnt += 1

if N > 0 :
    cnt = -1

print(cnt) 
