n, k, s = map(int, input().split())
res = [s] * k

if s == 10**9:
    res += [1] * (n-k)
else:
    res += [s+1] * (n-k)

print(*res)