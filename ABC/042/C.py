n, k = map(int, input().split())
d = list(map(int, input().split()))
s = set(d)

res = float("inf")


def dfs(curr):
    if curr >= n:
        global res
        res = min(res, curr)
        return

    curr *= 10
    for i in range(10):
        if i not in s:
            dfs(curr+i)


for i in range(1, 10):
    if i not in s:
        dfs(i)

print(res)
