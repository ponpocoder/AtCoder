n = int(input())
p = list(map(int, input().split()))

cnt = 0
for i in range(1, n-1):
    mx = max(p[i-1], p[i], p[i+1])
    mn = min(p[i-1], p[i], p[i+1])
    if p[i] == mx or p[i] == mn:
        continue
    cnt += 1

print(cnt)
