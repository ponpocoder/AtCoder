a, b, c = map(int, input().split())

d = c - a - b

if d > 0:
    if d**2 > 4 * a * b:
        print("Yes")
    else:
        print("No")
else:
    print("No")