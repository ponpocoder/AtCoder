x, y, a, b, c = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p.sort(reverse=True)
q.sort(reverse=True)

d = []

for i in range(x):
    d.append(p[i])
for i in range(y):
    d.append(q[i])
for i in range(c):
    d.append(r[i])

d.sort(reverse=True)

print(sum(d[:x+y]))