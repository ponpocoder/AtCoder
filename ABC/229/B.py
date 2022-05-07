import sys

a, b = map(int, input().split())

while a > 0 and b > 0:
    s = a % 10
    t = b % 10
    if s + t >= 10:
        print("Hard")
        sys.exit()
    a //= 10
    b //= 10

print("Easy")