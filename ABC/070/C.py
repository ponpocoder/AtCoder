from math import gcd

n = int(input())
curr = 1

for _ in range(n):
    t = int(input())
    curr = curr * t // gcd(curr, t)

print(curr)