n, m = map(int, input().split())
a = list(map(int, input().split()))
bc = []

for _ in range(m):
    x, y = map(int, input().split())
    bc.append((x, y))

a.sort()
bc.sort(key = lambda x: x[1], reverse = True)
p1, p2 = 0, 0
while p1 < n and p2 < m:
    b, c = bc[p2]
    while p1 < n and a[p1] < c and b > 0:
        a[p1] = c
        p1 += 1
        b -= 1
    p2 += 1

print(sum(a))