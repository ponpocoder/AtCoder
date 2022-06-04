from math import gcd

n, m = map(int, input().split())
l = n * m // gcd(n, m)

s = input()
t = input()

a = ["-1"] * l
b = ["-1"] * l

for i in range(n):
    idx = i * l // n
    a[idx] = s[i]

for i in range(m):
    idx = i * l // m
    b[idx] = t[i]

for i in range(l):
    if a[i] != "-1" and b[i] != "-1" and a[i] != b[i]:
        print(-1)
        exit()

print(l)