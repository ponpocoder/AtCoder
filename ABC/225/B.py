import sys

n = int(input())
edges = [[] for _ in range(n)]

for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

for edge in edges:
    if len(edge) == n - 1:
        print("Yes")
        sys.exit()

print("No")