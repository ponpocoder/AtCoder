n = int(input())
a = list(map(int, input().split()))

s = 0
for v in a:
    s ^= v

res = []
for v in a:
    res.append(s ^ v)

print(*res)
