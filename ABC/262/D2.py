from itertools import combinations

n = int(input())
a = list(map(int, input().split()))
mod = 998244353

p = [[0] * (n) for _ in range(n)]

for i in range(n):
    for j in range(1, n+1):
        p[i][j-1] = a[i] % j

res = 0
for i in range(n):
    curr = []
    for j in range(n):
        curr.append(p[j][i])
    for a in (list(combinations(curr, i+1))):
        if sum(a) % (i+1) == 0:
            res += 1
    res %= mod

print(res % mod)
