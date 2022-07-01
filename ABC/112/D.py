n, m = map(int, input().split())
s = set()
curr = m // n

for i in range(1, m):
    if i*i > m:
        break
    if m % i == 0:
        s.add(i)
        s.add(m // i)

p = sorted(list(s))

res = 1
for i in range(len(p)):
    if p[i] > curr:
        break
    res = max(res, p[i])

print(res)