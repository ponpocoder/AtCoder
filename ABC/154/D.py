n, k = map(int, input().split())
p = list(map(int, input().split()))

expects = [0] * n

def getEx(i):
    m = p[i]
    s = 0
    for j in range(1,m+1):
        s += j
    expects[i] = s / m

    return

for i in range(n):
    getEx(i)

s = [0] * (n+1)
for i in range(1, n+1):
    s[i] = s[i-1] + expects[i-1]

res = 0
for i in range(k, n+1):
    res = max(res, s[i] - s[i-k])

print(res)