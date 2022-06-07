from math import ceil

n, m = map(int, input().split())
res = 0

if m > 2 * n:
    res = n
    m -= 2 * n
    res += max(m//4 , 0)
else:
    res = m // 2
print(res)