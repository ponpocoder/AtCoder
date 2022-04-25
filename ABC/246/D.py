import sys
n = int(input())

def calc(a, b):
    return a**3 + a**2 * b + b**2 * a + b**3

res = float("inf")
for a in range(10 ** 6 + 1):    
    l, r = 0, a
    while l <= r:
        b = (l + r) // 2
        v = calc(a, b)
        if v >= n:
            res = min(res, v)
            r = b - 1
        else:
            l = b + 1

print(res)
