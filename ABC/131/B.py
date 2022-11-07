n, l = map(int, input().split())
s = 0

for i in range(n):
    s += l + i

res = 0
curr = 100000
for i in range(n):
    if abs(l+i) < curr:
        curr = abs(l+i)
        res = i

print(s-l-res)
