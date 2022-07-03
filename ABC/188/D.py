n, c = map(int, input().split())
s = []

for _ in range(n):
    a, b, d = map(int, input().split())
    s.append((a-1, d))
    s.append((b, -d))

s.sort()
res = 0
curr = 0
prev = 0

for x, y in s:
    res += min(curr, c) * (x - prev)
    prev = x
    curr += y

print(res)
