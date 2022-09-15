n = int(input())
x = list(map(int, input().split()))

a, b, c = 0, 0, 0

for v in x:
    a += abs(v)
    b += v**2
    c = max(c, abs(v))

print(a)
print(b**0.5)
print(c)
