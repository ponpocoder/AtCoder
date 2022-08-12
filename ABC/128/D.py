n, k = map(int, input().split())
v = list(map(int, input().split()))
res = 0

for l in range(k+1):
    for r in range(k+1-l):
        if l + r > n:
            break
        d = k - l - r
        curr = 0
        b = []
        for i in range(l):
            curr += v[i]
            b.append(v[i])

        for i in range(r):
            curr += v[n-1-i]
            b.append(v[n-1-i])

        b.sort()
        for i in range(min(d, len(b))):
            if b[i] >= 0:
                break
            curr -= b[i]

        res = max(res, curr)

print(res)
