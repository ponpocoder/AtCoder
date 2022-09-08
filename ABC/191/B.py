n, x = map(int, input().split())
a = list(map(int, input().split()))
res = []

for v in a:
    if v == x:
        continue
    res.append(v)

print(*res)

