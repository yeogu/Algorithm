import math


def CheckPaper(paper, x, y, n):
    global whiteConfetti, blueConfetti
    value = 0
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j]:
                value += 1
    if not value:
        whiteConfetti += 1
    elif value == n ** 2:
        blueConfetti += 1
    else:
        CheckPaper(paper, x, y, n // 2)                     # left top
        CheckPaper(paper, x + n // 2, y, n // 2)            # right top
        CheckPaper(paper, x, y + n // 2, n // 2)            # left bottom
        CheckPaper(paper, x + n // 2, y + n // 2, n // 2)   # right bottom

n = int(input())

paper = []
for i in range(n):
    paper.append(list(map(int, input().split())))

whiteConfetti = 0
blueConfetti = 0

CheckPaper(paper, 0, 0, n)

print(whiteConfetti)
print(blueConfetti)