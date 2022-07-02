from math import ceil

n, x = map(int, input().split())
ab = []

for _ in range(n):
    a, b = map(int, input().split())
    ab.append((a, b))

s = [0] * n
for i in range(1, n):
    a, b = ab[i-1]
    s[i] = s[i-1] + a + b

mn = ab[0][0] + ab[0][1] * x
idx = 0
for i in range(1, min(x, n)):
    curr = s[i] + ab[i][0] + ab[i][1] * (x-i)
    if curr < mn:
        mn = curr
        idx = i

print(mn)