a, b, c, d, e, f, x = map(int, input().split())

t1 = x // (a + c)
n = a * t1 + min(a, x - (a + c) * t1)

t2 = x // (d + f)
m = d * t2 + min(d, x - (d + f) * t2)

v = b * n
w = e * m

if v > w:
    print("Takahashi")
elif v < w:
    print("Aoki")
else:
    print("Draw")