n = int(input())

s = set()
t = []
for _ in range(n):
    x, y = map(int, input().split())
    s.add((x, y))
    t.append((x, y))

visited = set()


def dfs(x, y):
    if (x, y) not in s or (x, y) in visited:
        return False
    visited.add((x, y))
    dfs(x-1, y-1)
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    dfs(x+1, y)
    dfs(x+1, y+1)
    return True


res = 0
for x, y in s:
    if dfs(x, y):
        res += 1

print(res)
