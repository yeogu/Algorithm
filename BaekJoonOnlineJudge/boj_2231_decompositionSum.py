n = input()
strlen = len(n)
n = int(n)
minResult = n
for i in range(1, n - 1):
    strI = str(i)
    iLen = len(strI)
    sum = i
    for j in range(0, iLen):
        curNum = int(strI[j])
        sum += curNum
    if i < minResult and sum == n:
        minResult = i

if minResult == n:
    print(0)
else:
    print(minResult)