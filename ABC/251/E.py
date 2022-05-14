n = int(input())
a = list(map(int, input().split()))

def getCost(array):
    if len(array) <= 2:
        return min(array)

    dp = [float("inf")] * len(array)

    dp[0] = array[0]
    dp[1] = array[1]
    for i in range(2, len(array)):
        dp[i] = min(dp[i-2] + array[i], dp[i-1] + array[i])
        
    return dp[-1]

res1 = getCost(a)
res2 = getCost([a[-1]] + a[:-1])
res = min(res1, res2)
print(res)