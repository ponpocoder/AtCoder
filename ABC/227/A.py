n, k, a = map(int, input().split())
k += a - 1
k %= n

print(k if k != 0 else n)