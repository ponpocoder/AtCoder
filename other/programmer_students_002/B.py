n = int(input())
d = list(map(int, input().split()))
mod = 998244353
res = 0

if d[0] != 0:
    print(0)
    exit()

curr = 0
for i in range(1, n):
    curr = max(curr, d[i])
    if d[i] == 0 or d[i] > n:
        print(0)
        exit()

cnt = [0] * (curr+1)

for v in d:
    cnt[v] += 1

res = 1
for i in range(1, curr+1):
    res *= cnt[i-1] ** cnt[i]
    res %= mod

print(res)
