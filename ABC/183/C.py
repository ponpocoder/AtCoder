n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]

res = 0
used = set()


def dfs(c, i):
    if len(used) == n:
        c += t[i][0]
        global res
        if c == k:
            res += 1
        return

    for j in range(n):
        if j in used:
            continue
        used.add(j)
        dfs(c+t[i][j], j)
        used.remove(j)


used.add(0)
dfs(0, 0)
print(res)
