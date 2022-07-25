n = int(input())
c = list(map(int, input().split()))

mod = 10**9 + 7

c.sort()

res = 1
curr = 0
remain = 0
for i in range(n):
    remain = c[i] - curr
    res *= remain
    res %= mod
    curr += 1

print(res)
