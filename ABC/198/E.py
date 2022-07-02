import sys
sys.setrecursionlimit(10**6)

n = int(input())
c = list(map(int, input().split()))
graph = [[] for i in range(n)]

for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

cnt = [0] * (10**5+1)
s = [0] * n


def dfs(curr, prev):
    cnt[c[curr]] += 1

    for dest in graph[curr]:
        if dest != prev:
            dfs(dest, curr)

    if cnt[c[curr]] == 1:
        s[curr] += 1
    cnt[c[curr]] -= 1

dfs(0, -1)

for i in range(n):
    if s[i]:
        print(i+1)