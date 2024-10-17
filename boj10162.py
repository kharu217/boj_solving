T = int(input())

A = 300
B = 60
C = 10

A_cnt = 0
B_cnt = 0
C_cnt = 0

cnt = 0

while T >= A:
    T -= A
    A_cnt += 1
while T >= B :
    T -= B
    B_cnt += 1
while T >= C :
    T -= C
    C_cnt += 1

if T > 0 :
    print(-1)
else : print(A_cnt, B_cnt, C_cnt)
