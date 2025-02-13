n = int(input())
dp = [0] * 100001
dp[0] = 1
dp[1] = 2
dp[2] = 4

for i in range(n) :
    s = int(input())
    for a in range(3, s) :
        dp[a] = dp[a-1] + dp[a-2] + dp[a-3]
    print(dp[s-1])
