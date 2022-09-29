a, b, c, k = map(int, input().split())

one = min(k, a)
k = max(0, k - a)
zero = min(k, b)
k = max(0, k - b)
minus = min(k, c)

print(one-minus)
