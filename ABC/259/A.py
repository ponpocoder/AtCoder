n, m, x, t, d = map(int, input().split())
res = t 

if m <= x:
    res -= d * (min(n, x) - m)

print(res)