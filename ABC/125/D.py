n = int(input())
a = list(map(int, input().split()))
cnt = 0
mn = float("inf")
res = 0
for i in range(n):
    if a[i] < 0:
        cnt += 1
    res += abs(a[i])
    mn = min(mn, abs(a[i]))

if cnt % 2 == 1:
    res -= mn * 2
print(res)