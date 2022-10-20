n, k = map(int, input().split())
h = list(map(int, input().split()))

cnt = 0

for v in h:
    if v >= k:
        cnt += 1

print(cnt)
