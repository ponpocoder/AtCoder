n = int(input())
a = list(map(int, input().split()))

s = [0] * (n + 1)
for i in range(1, n+1):
    s[i] = s[i-1] + a[i-1]

res = 0
r = 0
xor = 0

for l in range(n):
    while r < n and xor ^ a[r] == s[r+1] - s[l]:
        xor ^= a[r]
        r += 1
    # print(l, r)
    res += r - l
    if l == r:
        r += 1
    xor ^= a[l]

print(res)
