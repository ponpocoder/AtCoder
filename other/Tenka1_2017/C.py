n = int(input())

for a in range(1, 3501):
    for b in range(1, 3501):
        x = n * a * b
        y = 4*a*b - n*(a+b)
        if y != 0 and x % y == 0 and x // y > 0:
            res = [a, b, x // y]
            break

print(*res)

