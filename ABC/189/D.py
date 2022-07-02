n = int(input())

dp = [1] * 2
for _ in range(n):
    s = input()
    p = dp
    dp = [0] * 2
    for j in range(2):
        for x in range(2):
            nj = j
            if s == "AND":
                nj &= x
            else:
                nj |= x
            dp[nj] += p[j]
    
print(dp[1])