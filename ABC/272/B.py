n, m = map(int, input().split())
s = set()
for i in range(n):
    for j in range(i+1, n):
        s.add((i+1, j+1))

for _ in range(m):
    y = list(map(int, input().split()))
    k = y[0]
    x = y[1:]
    for i in range(k):
        for j in range(k):
            a, b = x[i], x[j]
            if a > b:
                a, b = b, a
            if (a, b) in s:
                s.remove((a, b))

print("Yes" if len(s) == 0 else "No")
