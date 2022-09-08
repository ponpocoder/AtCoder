x, n = map(int, input().split())
p = list(map(int, input().split()))
s = set(p)

res = 10000
for i in range(200,-100, -1):
    if i in s:
        continue
    if abs(i - x) <= abs(res - x):
        res = i

print(res)
