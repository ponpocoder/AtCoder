n = int(input())
h = list(map(int, input().split()))

l = 0
res = 0
while l < n:
    while l < n and h[l] == 0:
        l += 1
    r = l
    if r == n:
        break
    while r < n and h[r] > 0:
        r += 1
    r -= 1
    for i in range(l, r+1):
        h[i] -= 1
    res += 1

print(res)