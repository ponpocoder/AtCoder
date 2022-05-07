n = int(input())
a = []

for _ in range(2*n - 1):
    curr = list(map(int, input().split()))
    a.append(curr)

pairs = []
used = [False] * 2*n
res = 0
def dfs(cnt, curr):
    if cnt == n:
        global res
        res = max(res, curr)
        return

    for i in range(2*n):
        if not used[i]:
            used[i] = True
            for j in range(i + 1, 2*n):
                if not used[j]:
                    used[j] = True
                    dfs(cnt+1, curr ^ a[i][j-i-1])
                    used[j] = False
            used[i] = False
            break
dfs(0, 0)
print(res)
    