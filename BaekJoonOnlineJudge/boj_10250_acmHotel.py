T = int(input())

for t in range(T):
    H, W, N = map(int, input().split())
    rooms = [[0 for _ in range(W)] for _ in range(H)]
    w, h = 0, 0
    for n in range(N):
        bFound = False
        for j in range(W):
            for i in range(H):
                if rooms[i][j] == 0:
                    bFound = True
                    rooms[i][j] = 1
                    w = j
                    h = i
                    break
            if bFound is True:
                break
    
    w += 1
    h += 1
    numW = ""
    numH = ""
    if w < 10:
        numW = "0" + str(w)
    else:
        numW = str(w)
    numH = str(h)
    print(numH + numW)