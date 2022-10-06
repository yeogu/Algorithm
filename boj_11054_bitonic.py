n = int(input())
a = list(map(int, input().split()))
updp = [1] * n
downdp = [1] * n

for i in range(n):
    for j in range(0, i):
        if a[i] > a[j]:
            updp[i] = max(updp[i], updp[j] + 1)

a.reverse()
for i in range(n):
    for j in range(0, i):
        if a[i] > a[j]:
            downdp[i] = max(downdp[i], downdp[j] + 1)

result = [0] * n
for i in range(n):
    result[i] = updp[i] + downdp[n-i-1] - 1

print(max(result))