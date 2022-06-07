n, m = map(int, input().split())
path = [set() for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    path[a].add(b)

for dest in path[1]:
    if n in path[dest]:
        print("POSSIBLE")
        exit()

print("IMPOSSIBLE")