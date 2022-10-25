k, x = map(int, input().split())

L, R = -1000000, 1000000

l = max(L, x-k+1)
r = min(R, x+k-1)

res = []
for i in range(l, r+1):
    res.append(i)

print(*res)
