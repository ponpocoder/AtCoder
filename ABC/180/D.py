x, y, a, b = map(int, input().split())

ex = 0

while True:
    if a*x >= y:
        break
    if a*x >= x+b:
        break
    x *= a
    ex += 1

ex += (y-1-x)//b

print(ex)