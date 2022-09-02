n, m = map(int, input().split())
key = []

for _ in range(m):
    a, b = map(int, input().split())
    c = list(map(int, input().split()))
    s = 0
    for v in c:
        s |= 1 << (v-1)

    key.append((a, s))

INF = 10**9
dp = [INF] * (1 << n)
dp[0] = 0
for i in range(1 << n):
    for j in range(m):
        a, s = key[j]
        curr = i | s
        cost = dp[i] + a
        dp[curr] = min(dp[curr], cost)

print(dp[-1] if dp[-1] != INF else -1)
