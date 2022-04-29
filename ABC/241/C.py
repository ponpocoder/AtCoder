import sys
n = int(input())
matrix = [input() for _ in range(n)]

def canForm(x, y, dx, dy):
    cnt = 0
    for i in range(6):
        if not (0 <= min(x, y) and max(x, y) < n):
            return False
        if matrix[x][y] == "#":
            cnt += 1
        x += dx
        y += dy
    return cnt >= 4

dx = [1, 0, -1, 1]
dy = [0, 1, -1, -1]

for i in range(n):
    for j in range(n):
        for x, y in zip(dx, dy):
            if canForm(i, j, x, y):
                print("Yes")
                sys.exit()
print("No")
