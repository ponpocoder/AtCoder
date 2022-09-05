a, b, n = map(int, input().split())

res = a * min(b-1, n) // b
print(res)
