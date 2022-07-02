n = int(input())
a = [input() for _ in range(n)]

def get(r, c, dire):
    res = ""
    for _ in range(n):
        res += a[r][c]
        r += dire[0]
        c += dire[1]
        if r >= n:
            r = 0
        if c >= n:
            c = 0
        if r < 0:
            r = n - 1
        if c < 0:
            c = n - 1
    
    return int(res)

res = 0
directions = [(0, 1), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, 0), (-1, -1), (0, -1)]

for i in range(n):
    for j in range(n):
        for dire in directions:
            res = max(res, get(i, j, dire))

print(res)