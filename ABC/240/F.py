t = int(input())

def calc():
    n, m = map(int, input().split())
    res = float("-inf")
    a, b = 0, 0
    for _ in range(n):
        x, y = map(int, input().split())
        res = max(res, a+b+x)
        if x < 0 and b > 0:
            i = - b // x
            if i < y:
                res = max(res, a + b * i + x * i * (i+1) // 2)
        a += b*y + x * y * (y+1) // 2
        b += x * y
        res = max(res, a)
    return res

res = []
for _ in range(t):
    res.append(calc())

for r in res:
    print(r)