n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)

parents = [i for i in range(n)]
ranks = [1] * n

def find(n):
    while n != parents[n]:
        parents[n] = parents[parents[n]]
        n = parents[n]
    return n

def union(n1, n2):
    p1, p2 = find(n1), find(n2)
    if p1 == p2:
        return 0
    if ranks[p1] > ranks[p2]:
        ranks[p1] += ranks[p2]
        parents[p2] = p1
    else:
        ranks[p2] += ranks[p1]
        parents[p1] = p2
    return -1

res = [0]
cnt = 0
for i in reversed(range(n)):
    cnt += 1
    for e in graph[i]:
        cnt += union(i, e)
    res.append(cnt)
    
for i in reversed(range(n)):
    print(res[i])
