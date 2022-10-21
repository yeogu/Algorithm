def p(n):
    dp = [0] * n
    if n > 0:
        dp[0] = 1
    if n > 1:
        dp[1] = 1
    if n > 2:
        dp[2] = 1
    if n > 3:
        dp[3] = 2
    if n > 4:
        dp[4] = 2
    if n > 5:
        dp[5] = dp[2] + dp[4]
    if n > 6:
        dp[6] = dp[1] + dp[5]
    if n > 7:
        dp[7] = dp[0] + dp[6]
    
    for i in range(8, n):
        dp[i] = dp[i-5] + dp[i-1]
    
    return dp[n-1]

t = int(input())

for i in range(t):
    n = int(input())
    result = p(n)
    print(result)