from cmath import sqrt
import math

def getDistance(x1, y1, x2, y2):
    dist = (x2-x1) * (x2-x1) + (y2-y1) * (y2-y1)
    dist = math.sqrt(dist)
    return dist

T = int(input())

for t in range(T):
    res = 0
    x1, y1, x2, y2 = map(int, input().split())
    N = int(input())
    
    distList1 = []
    distList2 = []
    for n in range(N):
        cx, cy, r = map(int, input().split())
        dist1 = getDistance(x1, y1, cx, cy)
        dist2 = getDistance(x2, y2, cx, cy)
        if dist1 < r and dist2 < r:
            pass
        elif dist1 < r:
            res += 1
        elif dist2 < r:
            res += 1
                
    print(res)