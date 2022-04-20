n, b, k = map(int, input().split())
c = list(map(int, input().split()))
mod = 10 **9 + 7
res = 0
def dfs(i, curr):
    if i == k:
        if curr % b == 0:
            res += 1
        return

    dfs(i + 1, curr)
    dfs(i + 1, curr + c[i])

dfs(0, 0)
print(res % mod)