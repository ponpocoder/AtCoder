n, k = map(int, input().split())
h = []
for _ in range(n):
    h.append(int(input()))

h.sort()
res = max(h)

for i in range(n-k+1):
    res = min(res, h[i+k-1]-h[i])

print(res)
