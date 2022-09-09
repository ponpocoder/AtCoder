a, b = map(int, input().split())

x, y = 0, 0

while a:
    x += a % 10
    a //= 10

while b:
    y += b % 10
    b //= 10

print(max(x, y))
