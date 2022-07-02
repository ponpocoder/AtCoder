n, m, q = map(int, input().split())
s = []

for _ in range(n):
    a, b = map(int, input().split())
    s.append((a, b))

x = list(map(int, input().split()))
s.sort(key=lambda x:x[1], reverse=True)

def get(l, r):
    y = []
    for i in range(m):
        if i < l or i > r:
            y.append(x[i])
    y.sort()
    p1 = 0
    p2 = 0
    used = [False] * len(y)

    res = 0
    for i in range(n):
        w, v = s[i]
        for j in range(len(y)):
            if w <= y[j] and not used[j]:
                res += v
                used[j] = True
                break
    return res

for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    print(get(l, r))