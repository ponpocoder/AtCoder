n = int(input())
a = list(map(int, input().split()))

order = []
for i, v in enumerate(a):
    order.append((v, i))

order.sort()
res = []

for i, j in order:
    res.append(j+1)

print(*res)

