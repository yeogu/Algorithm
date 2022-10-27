n, m = map(int, input().split())
num = list(map(int, input().split()))
maxVal = 0
for i in range(n):
    for j in range(i, n):
        for k in range(j, n):
            if i == j or i == k or j == k:
                continue
            else:
                sum = num[i] + num[j] + num[k]
                if sum > maxVal and sum <= m:
                    maxVal = sum

print(maxVal)
