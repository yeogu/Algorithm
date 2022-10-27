n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

result = road[0] * price[0]
curPrice = price[0]
for i in range(1, n-1):
    if price[i] < curPrice:
        curPrice = price[i]
    result += (curPrice * road[i])

print(result)