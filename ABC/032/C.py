n, k = map(int, input().split())

s = []
for _ in range(n):
    s.append(int(input()))

res = 0
curr = 1
l = 0
for r in range(n):
    if s[r] == 0:
        print(n)
        exit()
    curr *= s[r]
    while l < r and curr > k:
        curr //= s[l]
        l += 1
    if curr <= k:
        res = max(res, r-l+1)

print(res)
