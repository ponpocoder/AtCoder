n, k = map(int, input().split())
res = 0
for b in range(1, n+1):
    t = n // b
    res += t * max(b - k, 0)
    remain = n % b
    res += max(remain - k + 1, 0)

if k == 0:
    res -= n

print(res)