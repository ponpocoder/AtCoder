n, k = map(int, input().split())
cnt = [0] * n

for _ in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    for i in range(d):
        cnt[a[i]-1] += 1

res = 0
for v in cnt:
    if v == 0:
        res += 1

print(res)
