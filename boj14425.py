N, M = map(int, input().split())

S = {}
S_test = []

for n in range(N) :
    S[input()] = 0
for m in range(M) :
    S_test.append(input())

cnt = 0
for i in S_test :
    if i in S.keys() :
        cnt += 1
print(cnt)