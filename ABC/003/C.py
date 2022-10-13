n, k = map(int, input().split())
r = list(map(int, input().split()))
r.sort()
r = r[n-k:]
cnt = 0
curr = 0

for v in r:
    if v <= curr:
        continue
    cnt += 1
    curr = (curr+v)/2

print(curr)
