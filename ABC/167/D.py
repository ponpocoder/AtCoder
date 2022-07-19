n, k = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0
curr = 0
order = [-1] * n
visited = []

while True:
    if order[curr] != -1:
        break
    order[curr] = cnt
    visited.append(curr)
    cnt += 1
    curr = a[curr] - 1

cs = order[curr]
ce = cnt
cycle = ce - cs
if k <= cs:
    print(visited[k]+1)
else:
    rem = k - cs
    rem %= cycle
    print(visited[cs+rem]+1)