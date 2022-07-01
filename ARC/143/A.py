a, b, c = map(int, input().split())
mx = max(a, b, c)
mn = min(a, b, c)
s = a+b+c
md = s - mx - mn
cnt = 0
while mx > mn + 1 and mn >= 0:
        d = mx - mn
        cnt += d
        mx -= d
        md -= d
        tmp = mx
        s = mx + mn + md
        mx = max(mx, mn, md)
        mn = min(tmp, mn, md)
        md = s - mx - mn
if mx == mn:
    print(mn+cnt)
elif mx == mn + 1:
    if md == 0:
        print(-1)
    else:
        print(mn+1+cnt)
else:
    print(-1)