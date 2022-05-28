n = int(input())
a = list(map(int, input().split()))

one, two, three = 0, 0, 0

for v in a:
    if v == 1:
        one += 1
    elif v == 2:
        two += 1
    else:
        three += 1

dp = [[[-1] * (n+1) for _ in range(n+1)] for _ in range(n+1)]
dp[0][0][0] = 0

def getExpectation(p1, p2, p3):
    if dp[p1][p2][p3] != -1:
        return dp[p1][p2][p3]
    
    res = n
    if p1 > 0:
        res += p1 * getExpectation(p1-1, p2, p3)
    if p2 > 0:
        res += p2 * getExpectation(p1+1, p2-1, p3)
    if p3 > 0:
        res += p3 * getExpectation(p1, p2+1, p3-1)
    
    res /= p1 + p2 + p3
    dp[p1][p2][p3] = res
    return res

res = getExpectation(one, two, three)
print(res)