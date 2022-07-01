n, k = map(int, input().split())
d = set(map(int, input().split()))
res = []
def dfs(curr):
    if curr >= n:
        res.append(curr)
        return
    for i in range(10):
        if curr == 0 and i == 0:
            continue
        if i not in d:
            nc = curr * 10 + i
            dfs(nc)

dfs(0)
print(min(res))