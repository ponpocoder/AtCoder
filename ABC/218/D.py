n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
s = set(map(tuple, a))

res = 0
for i in range(n-1):
    currX, currY = a[i]
    for j in range(i+1, n):
        nextX, nextY = a[j]
        if currX == nextX or currY == nextY:
            continue
        if (currX, nextY) in s and (nextX, currY) in s:
            res += 1

print(res//2)