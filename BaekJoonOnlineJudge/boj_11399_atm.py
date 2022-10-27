n = int(input())
p = list(map(int, input().split()))

p.sort()
dp = [0] * n
dp[0] = p[0]
for i in range(1, n):
    dp[i] = dp[i-1] + p[i]

result = 0
for i in range(0, n):
    result += dp[i]

print(result)