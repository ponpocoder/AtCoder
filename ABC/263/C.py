n, m = map(int, input().split())

res = []


def dfs(last, curr):
    if len(curr) == n:
        res.append(curr.copy())
        return
    if last == m:
        return

    for i in range(last+1, m+1):
        curr.append(i)
        dfs(i, curr)
        curr.pop()


for i in range(1, m+1):
    dfs(i, [i])

for re in res:
    print(*re)
