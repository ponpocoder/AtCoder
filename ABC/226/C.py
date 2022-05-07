import sys
sys.setrecursionlimit(10**9)

n = int(input())
mastered  = [False] * n

t, k, a = [], [], []
for _ in range(n):
    array = list(map(int, input().split()))
    t.append(array[0])
    k.append(array[1])
    a.append(array[2:])

def dfs(curr):
    time = 0
    if not mastered[curr]:
        time += t[curr]
        mastered[curr] = True
    for s in a[curr]:
        if not mastered[s-1]:
            time += dfs(s-1)
            mastered[s-1] = True
    
    return time

print(dfs(n-1))


