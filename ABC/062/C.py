h, w = map(int, input().split())


def calc(r, c):
    res = r * c
    for i in range(r//2+1):
        a = i * c
        x = (r-i) // 2
        b = x * c
        d = (r-i-x) * c
        mx = max(a, b, d)
        mn = min(a, b, d)
        res = min(res, mx-mn)

        y = c // 2
        e = (r-i) * y
        f = (r-i) * (c-y)

        mx = max(a, e, f)
        mn = min(a, e, f)
        res = min(res, mx - mn)
    return res


res = min(calc(h, w), calc(w, h))
print(res)
