from math import gcd

n, m = map(int, input().split())
l = gcd(n, m)

s = input()
t = input()

for i in range(l):
    if s[n // l * i] != t[m // l * i]:
        print(-1)
        exit()

print(n * m // l)