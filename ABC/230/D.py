n, d = map(int, input().split())
pairs = [list(map(int, input().split())) for _ in range(n)]
pairs.sort(key=lambda x:x[1])
curr = 0
res = 0

for l, r in pairs:
    if curr < l:
        res += 1
        curr = r + d - 1

print(res)