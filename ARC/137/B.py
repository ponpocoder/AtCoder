n = int(input())
a = list(map(int, input().split()))

s = [0] * (n+1)

for i in range(1, n+1):
    if a[i-1] == 0:
        s[i] = s[i-1] + 1
    else:
        s[i] = s[i-1] - 1

mx  = 0
mn  = 0
lmx = lmn = 0
for r in range(1, n+1):
    mn = min(mn, s[r] - lmx)
    mx = max(mx, s[r] - lmn)
    lmx = max(lmx, s[r])
    lmn = min(lmn, s[r])

print(mx+abs(mn)+1)