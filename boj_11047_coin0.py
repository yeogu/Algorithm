n, k = list(map(int, input().split()))
a = [0] * n
for i in range(n):
    a[i] = int(input())
a.reverse()

result = 0
while True:
    for i in range(n):
        if (k - a[i]) >= 0:
            k -= a[i]
            result += 1
            break
    if k == 0:
        break

print(result)