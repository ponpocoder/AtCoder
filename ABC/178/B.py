a, b, c, d = map(int, input().split())

res = max(a*d, b*c, a*c, b*d)
print(res)
