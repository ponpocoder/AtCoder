n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
b = [0] * (m + 1)

b[m] = c[n + m] // a[n]
for i in range(m, -1, -1):
    b[i] = c[i + n] // a[n]
    for j in range(n + 1):
        c[i + j] -= a[j] * b[i]

print(*b)