n = int(input())
a = list(map(int, input().split()))

s = sum(a)
curr = 0
remain = s
res = float("inf")
l = 0
while l < n - 1:
    curr += a[l]
    remain -= a[l]
    res = min(res, abs(curr-remain))
    l += 1

print(res)