n, a, b = map(int, input().split())

x = n // (a + b)
remain = n - x * (a + b)
remain = min(a, remain)
res = a * x + remain
print(res)
