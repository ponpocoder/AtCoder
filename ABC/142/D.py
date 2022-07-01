from math import gcd
a, b = map(int, input().split())

c = gcd(a, b)
s = set()
s.add(1)

for i in range(2, c):
    if i*i > c:
        break
    while c % i == 0:
        s.add(i)
        c //= i
    
s.add(c)
print(len(s))