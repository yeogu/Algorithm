n = int(input())
result = 666
curNum = 666
count = 1
if n > 1:
    while count != n:
        curNum += 1
        strCurNum = str(curNum)
        strLen = len(strCurNum)
        for i in range(1, strLen - 1):
            if strCurNum[i-1] == '6' and strCurNum[i] == '6' and strCurNum[i+1] == '6':
                count += 1
                result = curNum
                break

print(result)