import sys
sys.setrecursionlimit(10**9)

s = input()
q = int(input())
curr = "ABC"

def dfs(t, k):
    if t == 0:
        return curr.index(s[k])
    if k == 0:
        return curr.index(s[0]) + t
    if k % 2 == 0:
        return dfs(t - 1, k // 2) + 1
    else:
        return dfs(t - 1, k // 2) + 2

for _ in range(q):
    t, k = map(int, input().split())
    print(curr[dfs(t, k - 1) % 3])