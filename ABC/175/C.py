x, k, d = map(int, input().split())
x = abs(x)
cnt = x // d

if k <= cnt:
    res = x - k*d
else:
    curr = x - d * cnt
    k -= cnt
    # print(curr, k)
    if k % 2 == 0:
        res = curr
    else:
        res = abs(curr-d)

print(res)