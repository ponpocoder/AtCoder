from collections import deque
from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)


n = int(input())
dic = defaultdict(list)

for _ in range(n):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

res = 1
visited = set()


def dfs(curr):
    if curr in visited:
        return
    visited.add(curr)
    global res
    res = max(res, curr)
    for dest in dic[curr]:
        dfs(dest)


dfs(1)
print(res)
