import math
N, K = map(int, input().split())
people = list(map(int, input().split()))

minS = 0xFFFFFFFF
for k in range(K, N+1):
    #k개 인형을 선택(연속적으로)
    i = 0
    while True:
        if i+k > N:
            break
        sumOfPeople = 0
        for sIdx in range(i, i+k):
            sumOfPeople += people[sIdx]
        #평균
        m = sumOfPeople / k

        #분산
        d = 0
        for sIdx in range(i, i+k):
            d += (people[sIdx] - m) ** 2
        d /= k
        #표준편차
        s = math.sqrt(d)
        minS = min(s, minS)
        i += 1

print(minS)