n, m, k = map(int, input().split())
mod = 998244353
res = 0

def dfs(curr, i):
    global res
    if curr <= k:
        res += 1
    if curr > k:
        return

    for j in range(i, i+n):
        dfs(curr + j, i)

for i in range(1, m - n + 1):
    dfs(0, i)
res %= mod
print(res)