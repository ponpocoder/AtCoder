x, a, d, n = map(int, input().split())

if d == 0:
    print(abs(x-a))
elif x >= a and d < 0:
    print(abs(x-a))
elif x <= a and d > 0:
    print(abs(x-a))
elif x >= a and d > 0 and x > a + (n-1) * d:
    print(x - a - (n -1) * d)
elif x <= a and d < 0 and x < a + (n -1) * d:
    print(abs(x - a - (n - 1) * d))
else:
    y = (x - a) // d
    curr = a + d * y
    curr2 = a + d * (y+1)
    res = min(abs(x -curr), abs(curr2 - x))
    print(res)