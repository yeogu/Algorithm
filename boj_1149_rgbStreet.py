from sys import stdin

n = int(input())
dp = [[0 for _ in range(3)] for _ in range(n)]

cost = []
for i in range(n):
    cost.append(list(map(int, input().split())))

for i in range(n):
    if i == 0:
        dp[i][0] = cost[i][0]
        dp[i][1] = cost[i][1]
        dp[i][2] = cost[i][2]
    else:
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

print(min(dp[n-1]))