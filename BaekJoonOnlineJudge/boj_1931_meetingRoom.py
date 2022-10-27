n = int(input())
meetings = []
for i in range(n):
    temp = list(map(int, input().split()))
    meetings.append(temp)

meetings.sort(key = lambda x: x[0])
meetings.sort(key = lambda x: x[1])
prev = 0
result = 1

end = meetings[0][1]
for i in range(1, n):
    if meetings[i][0] >= end:
        result += 1
        end = meetings[i][1]
print(result)