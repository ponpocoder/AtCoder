from math import gcd

n, s = map(int, input().split())
x = list(map(int, input().split()))
res = 0
for v in x:
    res = gcd(res, v-s)

print(res)