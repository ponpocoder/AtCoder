n = int(input())
mod = 10007
one, two, thr = 0, 0, 1

if n == 1:
    print(one)
elif n == 2:
    print(two)
elif n == 3:
    print(thr)
else:
    for _ in range(n-3):
        tmp = thr
        thr = one + two + thr
        one = two
        two = tmp
        thr %= mod

    print(thr)
# dp = [-1] * (n+2)
# dp[0] = 0
# dp[1] = 0
# dp[2] = 1


# def trib(i):
#     if dp[i] != -1:
#         return dp[i]
#     dp[i] = trib(i-1) + trib(i-2) + trib(i-3)
#     dp[i] %= mod
#     return dp[i]


# print(trib(n-1))
