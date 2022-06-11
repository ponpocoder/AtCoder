n = int(input())
u = []

for _ in range(n):
    x, y = map(int, input().split())
    s = x - y 
    t = x + y
    u.append((s, t))

u.sort(key=lambda x:x[1])

res = n
curr = u[0][1]

for i in range(1, n):
    l, r = u[i]
    if l >= curr:
        curr = r
    else:
        res -= 1

print(res)