n, m = map(int, input().split())
b = 0
if n % 2:
    n -= 1
    m -= 3
    b += 1
for i in range(n):
    if 2 * i + 4 * (n - i) == m:
        print(i, b, n-i)
        exit()
print(-1, -1, -1)
