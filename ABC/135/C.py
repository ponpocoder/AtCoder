n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

curr = 0
remain = 0
cnt = 0
for i in range(n+1):
    if remain:
        cnt += min(a[i], remain)
        a[i] = max(a[i] - remain, 0)
    if i < n:
        cnt += min(a[i], b[i])
        remain = max(0, b[i]-a[i])

print(cnt)
