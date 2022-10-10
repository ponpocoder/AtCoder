n, m = map(int, input().split())
x = (n % 12 + m / 60) / 12
y = m / 60

angle = abs(x-y) * 360
print(min(360-angle, angle))
