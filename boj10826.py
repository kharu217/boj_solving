n = int(input())
DP = [0] * 100001

for i in range(n+1) :
    if i == 0 :
        DP[0] = 0
    elif i == 1 :
        DP[1] = 1
    else :
        DP[i] = DP[i - 1] + DP[i -2]
print(DP[n])
