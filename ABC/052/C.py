n = int(input())
mod = 10**9 + 7
cnt = [0] * (n+1)

for i in range(1, n + 1):
    for j in range(2, i):
        if j*j > i:
            break
        while i % j == 0:
            cnt[j] += 1
            i //= j
    cnt[i] += 1

res = 1
for i in range(2, n+1):
    if cnt[i]:
        res *= cnt[i] + 1
        res %= mod

print(res)