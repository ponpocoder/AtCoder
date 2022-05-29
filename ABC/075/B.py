h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
m = s.copy()

def findBomb(i, j):
    res = 0
    if i > 0 and s[i-1][j] == "#":
        res +=1
    if j > 0 and s[i][j - 1] == "#":
        res +=1
    if j < w-1 and s[i][j + 1] == "#":
        res +=1
    if i > 0 and j > 0 and s[i-1][j-1] == "#":
        res +=1
    if i > 0 and j < w - 1 and s[i-1][j+1] == "#":
        res +=1
    if i < h-1 and s[i+1][j] == "#":
        res +=1
    if i < h-1 and j > 0 and s[i+1][j-1] == "#":
        res +=1
    if i < h-1 and j < w-1 and s[i+1][j+1] == "#":
        res +=1

    m[i][j] = str(res)

for i in range(h):
    for j in range(w):
        if m[i][j] != "#":
            findBomb(i, j)

for r in m:
    print("".join(r))