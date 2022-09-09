n = int(input())

dp = [0] * n

for i in range(n):
    if i == 0 or i == 1:
        dp[i] = 1
    else:
        dp[i] = dp[i-2] + dp[i-1]


print(max(dp))