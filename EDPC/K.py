n, k = map(int, input().split())
a = list(map(int, input().split()))

dp = [False] * (k + 1)
for i in range(k+1):
    for j in range(n):
        if i - a[j] >= 0 and dp[i - a[j]] == False:
            dp[i] = True
            break

if dp[k]:
    print("First")
else:
    print("Second") 