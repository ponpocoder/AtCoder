n, a, b = map(int, input().split())


mn = a*(n-1) + b
mx = b*(n-1) + a
res = mx - mn + 1

if a > b or (n == 1 and a != b):
    print(0)
else:
    print(res)