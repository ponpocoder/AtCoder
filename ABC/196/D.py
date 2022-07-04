h, w, a, b = map(int, input().split())

used = [[False] * w for _ in range(h)]

def dfs(r, c, a, b):
    if a < 0 or b < 0:
        return 0
    if c == w:
        r += 1
        c = 0
    if r == h:
        return 1
    if used[r][c]:
        return dfs(r, c+1, a, b)
    
    curr = 0
    used[r][c] = True
    curr += dfs(r, c+1, a, b-1)
    if c + 1 < w and not used[r][c+1]:
        used[r][c+1] = True
        curr += dfs(r, c+1, a-1, b)
        used[r][c+1] = False
    if r + 1 < h and not used[r+1][c]:
        used[r+1][c] = True
        curr += dfs(r, c+1, a-1, b)
        used[r+1][c] = False
    used[r][c] = False
    
    return curr

print(dfs(0, 0, a, b))