x = int(input())
parent = 1
child = 1

k = 0
sumSmall = 0
sumBig = 0
for i in range(1, x + 1):
    sumSmall = ((i - 1) * i) / 2
    sumBig = (i * (i + 1)) / 2
    if sumSmall < x and x <= sumBig:
        k = i
        break

if k != 0:
    nmg = x - sumSmall - 1
    if k % 2 == 0:
        parent = k - nmg
        child = 1 + nmg
    else:
        parent = 1 + nmg
        child = k - nmg

child = int(child)
parent = int(parent)
print(str(child) + "/" + str(parent))