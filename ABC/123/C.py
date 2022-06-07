from math import ceil

n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

mn = min(a, b, c, d, e)
res = ceil(n/mn) + 4
print(res)