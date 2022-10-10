n, k = map(int, input().split())

x = (k-1) * (n-k) * 6 + (k-1) * 3 + (n-k) * 3 + 1
y = n * n * n

print(x/y)
