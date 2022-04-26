import sys
n = int(input())
x = n
while True:
    l = int(x ** (1 / 3))
    for a in range(l + 1):
        for b in range(a, l + 1):
            if x == a**3 + a**2*b + a*b**2 + b**3:
                print(x)
                sys.exit()
    x += 1