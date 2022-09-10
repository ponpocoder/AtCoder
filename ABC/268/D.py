n, m = map(int, input().split())

s = [input() for _ in range(n)]
temp = []
t = set()
used = set()
for _ in range(m):
    t.add(input())


def dfs(curr):
    if len(curr) == n:
        temp.append(curr.copy())
        return
    for i in range(n):
        if i in used:
            continue
        curr.append(s[i])
        used.add(i)
        dfs(curr)
        used.remove(i)
        curr.pop()


# print(temp)
dfs([])


def solve(curr, i, x, remain):
    if i == len(x):
        if curr[-1] != "_" and curr not in t:
            res.append(curr[:])
        return
    if len(curr) > 16:
        return
    curr += x[i]
    if i < len(x) - 1:
        curr += "_"
    solve(curr, i+1, x, remain)
    for j in range(1, remain+1):
        curr += "_"
        solve(curr, i+1, x, remain - j)


res = []
for x in temp:
    remain = 16 - (2 * len(x) - 1)
    if remain < 0:
        continue
    solve("", 0, x, remain)

for v in res:
    if 3 <= len(v) <= 16:
        print(v)
        exit()

print(-1)
