n, m = map(int, input().split())
s = [input() for _ in range(n)]

res = 0

for i in range(n):
    t = set()
    for idx, c in enumerate(s[i]):
        if c == 'o':
            t.add(idx)
    for j in range(i+1, n):
        u = t.copy()
        for idx, c in enumerate(s[j]):
            if c == 'o':
                u.add(idx)
        if len(u) == m:
            res += 1

print(res) 
